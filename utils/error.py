class Errors:
    E_400: int = 400
    E_400_DESC: str = "The server couldn't understand your request. Please check your input and try again."
    
    E_403: int = 403
    E_403_DESC: str = "You don't have permission to access this page."
    
    E_404: int = 404
    E_404_DESC: str = "The page you are looking for doesn't exist. It may have been moved or deleted."
    
    E_500: int = 500
    E_500_DESC: str = "Something went wrong on our server. Please try again later."