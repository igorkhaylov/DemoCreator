/**
 * @license Copyright (c) 2003-2021, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
    config.contentsCss = 'fonts.css';

    // config.font_names = 'Arial/Arial, Helvetica, sans-serif;' +
    // 'Comic Sans MS/Comic Sans MS, cursive;' +
    // 'Courier New/Courier New, Courier, monospace;' +
    // 'Georgia/Georgia, serif;' +
    // 'Lucida Sans Unicode/Lucida Sans Unicode, Lucida Grande, sans-serif;' +
    // 'Tahoma/Tahoma, Geneva, sans-serif;' +
    // 'Times New Roman/Times New Roman, Times, serif;' +
    // 'Trebuchet MS/Trebuchet MS, Helvetica, sans-serif;' +
    // 'Verdana/Verdana, Geneva, sans-serif;' +
    // 'Dekers/dekers_true';

    config.font_names = 'CyrillicOld;' + config.font_names
    // config.font_names = config.font_names + 'CyrillicOld';
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
};
