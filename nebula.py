class Seafoam(Base):
    def _init_(
        self,
        *,
        primary_hue: colors.Color | str = colors.purple,  # Base hue for purples
        secondary_hue: colors.Color | str = colors.blue,  # Optional secondary hue
        neutral_hue: colors.Color | str = colors.blue,
        spacing_size: sizes.Size | str = sizes.spacing_md,
        radius_size: sizes.Size | str = sizes.radius_md,
        text_size: sizes.Size | str = sizes.text_lg,
        font: fonts.Font
        | str
        | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("Quicksand"),
            "ui-sans-serif",
            "sans-serif",
        ),
        font_mono: fonts.Font
        | str
        | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("IBM Plex Mono"),
            "ui-monospace",
            "monospace",
        ),
    ):
        super()._init_(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        super().set(
            body_background_fill="linear-gradient(45deg, #5d3fd3, #9b5fd3, #d335ff, #bb33ff)",
            body_background_fill_dark="linear-gradient(45deg, #3b2870, #5d3fd3, #9b5fd3, #d335ff)",
            button_primary_background_fill="linear-gradient(90deg, #5d3fd3, #3b2870)",
            button_primary_background_fill_hover="linear-gradient(90deg, #9b5fd3,  #3b2870)",
            button_primary_text_color="white",
            button_primary_background_fill_dark="linear-gradient(90deg, #3b2870, #ffffff)",
            slider_color="#d335ff",
            slider_color_dark="#5d3fd3",
            block_title_text_weight="600",
            block_border_width="3px",
            block_shadow="*shadow_drop_lg",
            button_shadow="*shadow_drop_lg",
            button_large_padding="32px",
        )


seafoam = Seafoam()
