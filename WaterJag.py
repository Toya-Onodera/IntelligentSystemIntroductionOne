# coding: utf-8

class WaterJag:
    def __init__ (self, l_cap_size, m_cap_size, target_capacity):
        self.l_cap = l_cap_size
        self.m_cap = m_cap_size
        self.target = target_capacity
        
    def start(self):
        self.calc(0, 0, 1)
        
    def calc(self, l_capacity, m_capacity, state):
        # 目的の容量を得ることができた場合
        if l_capacity == self.target:
            return True
        
        # 水差し問題を解く、流れとして
        # 1: L カップに水を、満タンに入れる
        # 2: L カップから M カップに水を入れるだけ入れる
        # 3: M カップに入っている水を捨て、L カップに残っている水を M カップに移す
        # 4: 1 ~ 3 を繰り返すと目的の容量の水が得られる
        if (state == 1):
            l_cap = self.l_cap
            m_cap = m_capacity
            state = 2
            
        elif (state == 2):
            l_cap = l_capacity - (self.m_cap - m_capacity)
            m_cap = self.m_cap
            state = 3
            
        elif (state == 3):
            m_cap = l_capacity
            l_cap = 0
            state = 1
            
        print(f"Lカップ容量：{l_cap}, Mカップ容量：{m_cap}")

        self.calc(l_cap, m_cap, state)
        
_water_jag = WaterJag(7, 5, 4)
_water_jag.start()
