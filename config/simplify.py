# -*- coding: utf-8 -*-
f = open('test.txt', encoding='utf-8')
line = f.readline()
filename = 'get_method.txt'
filename2 = 'do_method.txt'
f1 = open(filename, 'w')
f2 = open(filename2, 'w')
f1.truncate()
f2.truncate()

while line:
    print(line[:-1])
    with open(filename, 'a') as fl:
        if line.startswith('#'):
            fl.write(line)
        elif line.startswith(' '):
            fl.write(line)
        elif line.startswith('_'):
            a = ''.join((line.split(' '))[:1])
            if not(a.split('_'))[1].endswith('s'):
                fl.write('def get{}(self):\n'.format(a))
                fl.write('    return self.find_Element(self.{})\n'.format(a))
            else:
                fl.write('def get{}(self):\n'.format(a))
                fl.write('    return self.find_Elements(self.{})\n'.format(a))
        else:
            print('1232133')
    with open(filename2, 'a') as fr:
        if line.startswith('#'):
            fr.write(line)
        elif line.startswith(' '):
            fr.write(line)
        elif line.startswith('_btn'):
            a = ''.join((line.split(' '))[:1])
            fr.write('def click{}(self):\n'.format(a))
            fr.write('    return self.click_element(self.get{}())\n'.format(a))
        elif line.startswith('_fbtn'):
            a = ''.join((line.split(' '))[:1])
            fr.write('def click{}(self):\n'.format(a))
            fr.write('    return self.move_click_element(self.get{}())\n'.format(a))
        elif line.startswith('_input'):
            a = ''.join((line.split(' '))[:1])
            fr.write('def sendkeys{}(self, value):\n'.format(a))
            fr.write('    return self.send_keys(self.get{}(), value)\n'.format(a))
        elif line.startswith('_show'):
            a = ''.join((line.split(' '))[:1])
            fr.write('def move_to{}(self):\n'.format(a))
            fr.write('    return self.move_to_element(self.get{}())\n'.format(a))
        elif line.startswith('_texts'):
            a = ''.join((line.split(' '))[:1])
            fr.write('def gettexts{}(self):\n'.format(a))
            fr.write('    return self.get_elements_values(self.get{}())\n'.format(a))
        elif line.startswith('_text'):
            a = ''.join((line.split(' '))[:1])
            fr.write('def gettexts{}(self):\n'.format(a))
            fr.write('    return self.get_element_value(self.get{}())\n'.format(a))
    line = f.readline()
fl.close()
fr.close()
f.close()
