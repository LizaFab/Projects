class RomNum:
    
    nums = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    syms = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    sub = ["I", "X", "C"]
    map = {key: value for key, value in zip(syms, nums)}
    
    double = [i for i in syms if len(i) > 1]
    single = [i for i in syms if len(i) == 1]
    
    def check_if_numeric(self, num):
        if not num.isdigit():
            print('Your input contains non-numeric characters.')
            return False
        return True

    def check_if_not_zero(self, num):
        if num == '0':
            print('There is no zero in the Roman numeral system.')
            return False
        return True
        
    def conversion_nr(self, num):
        rom = ''
        num = int(num)
        og_num = num
        i = len(self.syms) - 1
        while num:
            x = num // self.nums[i]
            num = num % self.nums[i]
            if x != 0:
                rom += self.syms[i] * x
            i -= 1
        print(f'The Roman numeral for {og_num} is {rom}.')
        

    def num_rom(self):
        # Input validation
        while True:
            num = input("Enter a number: ")
            if not self.check_if_numeric(num):
                continue
            if not self.check_if_not_zero(num):
                continue
            break
        
        self.conversion_nr(num)
    
    # ROMAN TO NUMBER
    
    def check_if_isalpha(self, rom):
        if not rom.isalpha():
            print('Your input contains invalid characters like Arabic digits.')
            return False
        return True
        
    def are_characters_correct(self, rom):
        s_set = set(self.single)
        rom = rom.upper()
        if not (set(rom).issubset(s_set)):
            print(f'Your input contains invalid characters: {set(rom).difference(s_set)}, which are not used in the Roman numeral system.')
            return False
        return True
        
    def vdl(self, rom):
        if rom.count('V') > 1 or rom.count('L') > 1 or rom.count('D') > 1:
            print('Invalid input. V, L, and D cannot appear more than once.')
            return False
        return True
    
    def triple(self, rom):
        # Remove M - can appear more than 3 times
        # Remove V, L, D - caught by another rule
        single_tri = ['I', 'X', 'C']
        for s in single_tri:
            if s * 4 in rom:
                print(f'Symbol {s} cannot appear more than 3 times in a row in a Roman numeral.')
                return False
        return True
    
    def char_order(self, rom):
        prev_val = 2000
        x = 0
        while x < len(rom):
            if x > 0:
                if rom[x:x+2] in self.map:
                    if self.map[rom[x:x+2]] > self.map[prev_val]:
                        print(f'The characters in your Roman numeral are out of order. {rom[x:x+2]} ({self.map[rom[x:x+2]]}) is greater than the previous value {prev_val} ({self.map[prev_val]}). Smaller values must follow larger ones.')
                        return False
                    prev_val = rom[x:x+2]
                    x += 1
                    
                elif rom[x:x+1] in self.map:
                    if self.map[rom[x:x+1]] > self.map[prev_val]:
                        print(f'The characters in your Roman numeral are out of order. {rom[x:x+1]} ({self.map[rom[x:x+1]]}) is greater than the previous value {prev_val} ({self.map[prev_val]}). Smaller values must follow larger ones.')
                        return False
                    prev_val = rom[x:x+1]
                    x += 1
    
            elif x == 0:
                if rom[x:x+2] in self.map:
                    prev_val = rom[x:x+2]
                elif rom[x:x+1] in self.map:
                    prev_val = rom[x:x+1]
                x += 1
        return True
    
    def rom_num(self):
        num = 0
        symbols = {}
        
        # Validation
        while True:
            rom = input('Enter a Roman numeral: ').upper()
            if not self.check_if_isalpha(rom):
                continue
            if not self.are_characters_correct(rom):
                continue
            if not self.vdl(rom):
                continue
            if not self.triple(rom):
                continue
            if not self.char_order(rom):
                continue
            break
        
        # Conversion
        og_rom = rom
        for d in self.double:
            if rom.count(d) != 0:
                symbols[d] = rom.count(d)
                rom = rom.replace(d, "")

        for s in self.single:
            if rom.count(s) != 0:
                symbols[s] = rom.count(s)

        for k, v in symbols.items():
            num += v * self.map[k]
        print(f'The Arabic number for {og_rom} is {num}.')


print('Arabic to Roman numeral converter:')
RomNum().num_rom()

print('Roman to Arabic numeral converter:')        
RomNum().rom_num()
