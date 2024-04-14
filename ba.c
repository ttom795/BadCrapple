#include <gb/gb.h>

extern char frames[][18][20];

const unsigned char combined_tile[] = {
	// white_tile
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    // black_tile
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF
};

void drawFrame(uint32_t frame_num) {
    uint8_t y, x;
	uint8_t white_tile_index = 0;
    uint8_t black_tile_index = 1;
	
	for (y = 0; y < 18; y += 1) {
		for (x = 0; x < 20; x += 1) {
			switch (frames[frame_num][y][x]) {
				case 0:
					set_bkg_tiles(x, y, 1, 1, &black_tile_index);
					break;
				case 1:
					set_bkg_tiles(x, y, 1, 1, &white_tile_index);
					break;
			}
		}
	}
}

void main(void) {
	uint8_t val = 0;
    SPRITES_8x8;
    DISPLAY_OFF;
	
	set_bkg_1bpp_data(0, 2, combined_tile); 
    drawFrame(0);
    
    SHOW_BKG;
    SHOW_SPRITES;
    DISPLAY_ON;

    while(1) {
		val += 1;
		delay(500);
		drawFrame(val);
        vsync();
    }
}
