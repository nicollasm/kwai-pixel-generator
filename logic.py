def generate_kwai_pixel_script(pixel_id, event):
    return f"<script>\n    kwaiq.instance('{pixel_id}').track('{event}');\n</script>"
