// Click-to-load YouTube facade. Nothing is requested from YouTube until the
// visitor actually asks for the video. Without JS the play button stays a
// plain link to youtube.com, so the page still works.
document.querySelectorAll('.video[data-video-id]').forEach(function (box) {
  var button = box.querySelector('.video-play');
  if (!button) return;

  button.addEventListener('click', function (event) {
    event.preventDefault();

    var frame = document.createElement('iframe');
    frame.src =
      'https://www.youtube-nocookie.com/embed/' +
      encodeURIComponent(box.dataset.videoId) +
      '?autoplay=1&rel=0';
    frame.title = box.dataset.title || 'Episode video';
    frame.allow =
      'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
    frame.allowFullscreen = true;
    frame.loading = 'eager';

    box.replaceChildren(frame);
    frame.focus();
  });
});
