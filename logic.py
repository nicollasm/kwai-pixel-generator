from ads_scripts import kwai_ads, facebook_ads

PLATFORMS = {
    "kwai_ads": kwai_ads.generate_pixel_script,
    "facebook_ads": facebook_ads.generate_pixel_script
}


def generate_pixel_script(platform, pixel_id, event):
    if platform not in PLATFORMS:
        raise ValueError("Plataforma desconhecida")

    return PLATFORMS[platform](pixel_id, event)
