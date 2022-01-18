/**
 * @license Copyright (c) 2003-2021, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
    config.contentsCss = 'fonts.css';
    config.font_names = 'CyrillicOldBold;' + config.font_names;
    // config.font_names = 'CyrillicOld;' + config.font_names;
};
