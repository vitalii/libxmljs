{
  'targets': [
    {
      'target_name': 'xmljs',
      'sources': [
        'src/libxmljs.cc',
        'src/xml_attribute.cc',
        'src/xml_document.cc',
        'src/xml_element.cc',
        'src/xml_namespace.cc',
        'src/xml_node.cc',
        'src/xml_sax_parser.cc',
        'src/xml_syntax_error.cc',
        'src/xml_xpath_context.cc',
      ],

      'cflags': [
        '<!@(xml2-config --cflags)'
	  ],

      'libraries': [
        '<!@(xml2-config --libs)'
	  ],

	  'cflags_cc=': [
		'-frtti', '-fexceptions'
	  ]
    }
  ]
}
