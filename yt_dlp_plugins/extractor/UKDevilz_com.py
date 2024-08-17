from yt_dlp.extractor.common import InfoExtractor
from yt_dlp.utils import ExtractorError, urljoin
from bs4 import BeautifulSoup


class UKDevilzPlusIE(InfoExtractor):
    IE_NAME = 'UKDevilzPlus'
    _VALID_URL = r'https?://(?:www\.)?(?:ukdevilz\.com|noodlemagazine\.com|tyler-brown\.com|mat6tube\.com|exporntoons\.net|actionviewphotography\.com)/watch/-?(?P<id>\d+_\d+)'

    def _get_meta_content(self, soup, property_name, transform=None):
        """Helper function to get and optionally transform the content of a meta tag."""
        meta_tag = soup.find('meta', property=property_name)
        if not meta_tag or not meta_tag.get('content'):
            return None
        content = meta_tag['content']
        return transform(content) if transform else content

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        soup = BeautifulSoup(webpage, 'html.parser')

        # Extract title
        title_elem = soup.find('title')
        title = title_elem.get_text(strip=True) if title_elem else None

        # Extract metadata using the helper function
        duration = self._get_meta_content(soup, 'video:duration', int)
        upload_date = self._get_meta_content(soup, 'ya:ovs:upload_date', lambda x: x.replace('-', ''))
        likes = self._get_meta_content(soup, 'ya:ovs:likes', int)
        view_count = self._get_meta_content(soup, 'ya:ovs:views_total', int)

        # Extract, deduplicate, strip, and sort tags
        tags = self._get_meta_content(
            soup, 
            'video:tag', 
            lambda x: sorted(set(tag.strip() for tag in x.split(',')), key=str.lower)
        )
        
        thumbnail = self._get_meta_content(soup, 'og:image')

        # Extract formats and VTT track
        script = soup.find('script', text=lambda t: t and 'window.playlist' in t)
        if not script:
            raise ExtractorError('Could not find video data in the page')

        json_data_str = script.string.split('window.playlist = ', 1)[1].split(';', 1)[0].strip()
        video_data = self._parse_json(json_data_str, video_id)

        formats = []
        vtt_url = None
        for source in video_data.get('sources', []):
            video_url = source.get('file')
            resolution_label = source.get('label')
            if video_url and resolution_label:
                formats.append({
                    'url': video_url,
                    'format_id': resolution_label,
                    'height': int(resolution_label) if resolution_label.isdigit() else None,
                    'ext': source.get('type', 'mp4'),
                })

        # Extract VTT track (thumbnails) and convert to absolute URL
        tracks = video_data.get('tracks', [])
        for track in tracks:
            if track.get('kind') == 'thumbnails':
                relative_vtt_url = track.get('file')
                vtt_url = urljoin(url, relative_vtt_url)  # Construct the absolute URL
                break

        return {
            'id': video_id,
            'title': title,
            'thumbnail': thumbnail,
            'formats': formats,
            'duration': duration,
            'upload_date': upload_date,
            'like_count': likes,
            'view_count': view_count,
            'tags': tags,
            'vtt_url': vtt_url,  # Add VTT URL to the output
        }


__all__ = ['UKDevilzPlusIE']
