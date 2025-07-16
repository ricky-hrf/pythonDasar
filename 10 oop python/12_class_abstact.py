from abc import ABC,abstractmethod

class Button(ABC):
  
  def __init__(self, set_link):
    self.link = set_link
  @abstractmethod
  def click(self):
    pass
class LinkButton(Button):
  
  def click(self):
    print(f"Link button clicked, opening {self.link}")
class SubmitButton(Button):
  
  def click(self):
    print(f"Submit button clicked, submitting form to {self.link}")
class ResetButton(Button):
  
  def click(self):
    print(f"Reset button clicked, resetting form at {self.link}")
# Example usage
if __name__ == "__main__":
  link_button = LinkButton("https://example.com")
  submit_button = SubmitButton("https://submit.com")
  reset_button = ResetButton("https://reset.com")

  link_button.click()
  submit_button.click()
  reset_button.click()


    