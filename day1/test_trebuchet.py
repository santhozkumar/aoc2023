from trebuchet import process_line



def test_process_line():
    assert(process_line('eightwo1one') == ('8', '1'))
    assert(process_line('3eight8') == ('3', '8'))
    assert(process_line('rgxjrsldrfmzq25szhbldzqhrhbjpkbjlsevenseven') == ('2', '7'))
    assert(process_line('3aeight5') == ('3', '5'))
    assert(process_line('sxbjdbtlnjrmlzgxneight') == ('8', '8'))
    

