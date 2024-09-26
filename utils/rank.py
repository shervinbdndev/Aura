class Ranks:
    RANK_1_EXP: int = 500_000
    RANK_1_NAME: str = 'Aura Apprentice'
    
    RANK_2_EXP: int = 1_000_000
    RANK_2_NAME: str = 'Aura Veteran'
    
    RANK_3_EXP: int = 2_000_000
    RANK_3_NAME: str = 'Aura Hero'
    
    RANK_4_EXP: int = 10_000_000
    RANK_4_NAME: str = 'Aura Legend'
    
    RANK_5_EXP: int = 50_000_000
    RANK_5_NAME: str = 'Aura Immortal'
    
    RANK_6_EXP: int = 200_000_000
    RANK_6_NAME: str = 'Aura Godlike'



class LegendaryRanks:
    L_RANK_1_EXP: int = 1_000_000_000
    L_RANK_1_NAME: str = 'Aura Celestial'
    
    L_RANK_2_EXP: int = 5_000_000_000
    L_RANK_2_NAME: str = 'Aura Divine'
    
    L_RANK_3_EXP: int = 20_000_000_000
    L_RANK_3_NAME: str = 'Aura Eternal'
    
    



class RankManager:
    def __init__(self) -> None:
        self.__user_rank = None
        self.user_true_rank = None
        self.__user_exp_needed_for_next_rank = None
        
    @property
    def user_rank(self) -> str:
        return self.__user_rank
    
    @user_rank.setter
    def user_rank(self, value: str) -> None:
        self.__user_rank = value
    
    @property
    def user_exp_needed_for_next_rank(self) -> int:
        return self.__user_exp_needed_for_next_rank
    
    @user_exp_needed_for_next_rank.setter
    def user_exp_needed_for_next_rank(self, value) -> None:
        self.__user_exp_needed_for_next_rank = value
        
    def setUserTrueRank(self) -> None:
        rank_list: list[str] = [
            'Aura Apprentice',
            'Aura Veteran',
            'Aura Hero',
            'Aura Legend',
            'Aura Immortal',
            'Aura Godlike',
            'Aura Celestial',
            'Aura Divine',
            'Aura Eternal',
        ]
        
        for rank in rank_list:
            if (rank == self.user_rank):
                self.user_true_rank = rank_list[rank_list.index(self.user_rank) - 1]
                break
        
    def setUserRank(self, user) -> None:
        if user.coins == -1:
            self.user_rank = 'Admin'
            return
        
        if user.coins >= LegendaryRanks.L_RANK_2_EXP:
            self.user_rank = LegendaryRanks.L_RANK_3_NAME
            self.user_exp_needed_for_next_rank = LegendaryRanks.L_RANK_3_EXP
            
        elif user.coins >= LegendaryRanks.L_RANK_1_EXP:
            self.user_rank = LegendaryRanks.L_RANK_2_NAME
            self.user_exp_needed_for_next_rank = LegendaryRanks.L_RANK_2_EXP
            
        elif user.coins >= Ranks.RANK_6_EXP:
            self.user_rank = LegendaryRanks.L_RANK_1_NAME
            self.user_exp_needed_for_next_rank = LegendaryRanks.L_RANK_1_EXP
            
        elif user.coins >= Ranks.RANK_5_EXP:
            self.user_rank = Ranks.RANK_6_NAME
            self.user_exp_needed_for_next_rank = Ranks.RANK_6_EXP
            
        elif user.coins >= Ranks.RANK_4_EXP:
            self.user_rank = Ranks.RANK_5_NAME
            self.user_exp_needed_for_next_rank = Ranks.RANK_5_EXP
            
        elif user.coins >= Ranks.RANK_3_EXP:
            self.user_rank = Ranks.RANK_4_NAME
            self.user_exp_needed_for_next_rank = Ranks.RANK_4_EXP
            
        elif user.coins >= Ranks.RANK_2_EXP:
            self.user_rank = Ranks.RANK_3_NAME
            self.user_exp_needed_for_next_rank = Ranks.RANK_3_EXP
            
        elif user.coins >= Ranks.RANK_1_EXP:
            self.user_rank = Ranks.RANK_2_NAME
            self.user_exp_needed_for_next_rank = Ranks.RANK_2_EXP
            
        else:
            self.user_rank = Ranks.RANK_1_NAME
            self.user_exp_needed_for_next_rank = Ranks.RANK_1_EXP