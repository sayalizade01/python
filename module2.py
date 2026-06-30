#Q40.
# class WaterPressurLowError(Exception):
#     pass
# class Sprinkler:
#     def water_crops(self):
#         print("General watering..")

# class DripIrrigation(Sprinkler):
#     def water_crops(self):
#          print("Drip irrigation:water released slowly at roots, saving water")

# class RotarySprinkler(Sprinkler):
#     def water_crops(self):
#         print("Rotary Sprinkler: Water is sprayed rapidly over a wide area.")

# try:
#     pressure=int(input("Enter water pressure in pis: "))

#     if pressure<20:
#         raise WaterPressurLowError("Water pressure to low")
#     systems=[DripIrrigation(),RotarySprinkler()]

#     for system in systems:
#         system.water_crops()

# except WaterPressurLowError:
#     print("Error:low")
#     print("System shutting down")

#Q39 . A role-playing game features various non-playable characters (NPCs). Design a 
# base class NPC with a method move(). Derive Merchant and Enemy classes. Through 
# polymorphism, the Merchant moves along predefined safe roads, while the Enemy 
# utilizes pathfinding algorithms to chase the player. Implement a custom PathBlockedError. 
# If an NPC attempts to move into a coordinate occupied by a wall or obstacle, raise the 
# exception, catch it, and force the NPC to stand still for one turn.

# class PathBlockedError(Exception):
#     pass
# class NCP:
#     def move(self):
#         print("Ncp is moving..")
# class merchant(NCP):
#     def move(self,position,block_positions):
#         print("Move along predefined safe roads")
        
#         if position in block_positions:
#             raise PathBlockedError("Path is blocked for merchants")
#         print("Merchants moved safely on predefined roads")
# class Enemy(NCP):
#     def move(self,position,block_position):
#         print("utilizes pathfinding algorithms")

#         if position in block_position:
#             raise PathBlockedError("Path is blocked")
#         print("Enmy moves towards  player")

# block_position=[(2,2),(3,3)]

# try:


#Q38A smart home integration manages window coverings. Create a base 
# class WindowCovering with a method adjust_blinds(). 
# Derive RollerBlind and VenetianBlind classes. Polymorphism dictates that Roller blinds roll 
# up and down vertically, while Venetian blinds rotate their slats horizontally to let light in. 
# Create a custom exception MotorJammedError. If the electric motor draws excess current 
# during adjustment, raise the exception, catch it, and immediately cut power to prevent a 
# fire hazard.
# class MotorJammedError(Exception):
#     pass
# class WindowCovering:
#     def adjust_blind(self):
#         print("Adjusting blinds...")

# class RollerBlind(WindowCovering):
#     def adjust_blind(self,current):
#         print("Roll up and down vertically")
#     if current >10:
#         raise MotorJammedError("motor jamed ")
#     print("adjust successfully")
# class VenetianBlind(WindowCovering):
#     def adjust_blind(self,current):
#         print("Roll horizontally")
#         if current>10:
#             raise MotorJammedError("Motor jammed ")
        
# devices = [
#     (RollerBlind(), 12),   # high current → error
#     (VenetianBlind(), 5)   # safe
# ]
# for device,curr in devices:
#     try:
#      device.adjust_blinds(curr)
#     except MotorJammedError:
#      print("Power cutt")

#Q39 A software updater handles large background downloads. Create a base 
# class Downloader with a method fetch_file(). Derive HTTPDownloader and FTPDownloader. Use 
# polymorphism: HTTP uses secure web requests, while FTP connects directly to a file 
# server port. Implement a custom exception DiskFullError. During the fetch_file() process, if 
# the available system storage drops below the incoming file size, raise the exception, 
# catch it, and pause the download gracefully

# Step 1: Custom Exception
# class DiskFullError(Exception):
#     pass


# # Step 2: Base Class
# class Downloader:
#     def fetch_file(self):
#         print("Downloading file...")


# # Step 3: Derived Classes
# class HTTPDownloader(Downloader):
#     def fetch_file(self, file_size, available_space):
#         print("HTTP Downloader: Using secure web request...")

#         if available_space < file_size:
#             raise DiskFullError("Not enough disk space for HTTP download!")

#         print("File downloaded successfully via HTTP.")


# class FTPDownloader(Downloader):
#     def fetch_file(self, file_size, available_space):
#         print("FTP Downloader: Connecting to file server port...")

#         if available_space < file_size:
#             raise DiskFullError("Not enough disk space for FTP download!")

#         print("File downloaded successfully via FTP.")


# # Step 7: Polymorphism with exception handling
# downloads = [
#     (HTTPDownloader(), 500, 300),  # not enough space → error
#     (FTPDownloader(), 200, 500)    # enough space → success
# ]

# for downloader, size, space in downloads:
#     try:
#         downloader.fetch_file(size, space)
#     except DiskFullError:
#         print("⚠️ Disk full! Pausing download safely.\n")


# Q36 A pet care clinic manages records digitally. Design a base class Pet with a 
# method schedule_appointment(). Create derived classes Dog and Cat. Use polymorphism: 
# Dog appointments require an automatic booking for a rabies shot, while Cat 
# appointments require a feline leukemia shot. Implement a custom VaccinationOverdueError. 
# If a pet has not visited the clinic in over 2 years, raise the exception, catch it, and flag 
# the appointment as "High Priority".

# class VaccinationOverdueError(Exception):
#     pass
# class pet:
#     def schedule_appointment(self):
#         print()

# class Dog(pet):
#     def schedule_appointment(self,years):
#         print("add rabies shot")
#         if years>2:
#             raise VaccinationOverdueError("Dog vaccination overdue!")
#         print("Dog appointment scheduled")

# class cat(pet):
#      def schedule_appointment(self,years):
#         print("frlin Leukemia")
#         if years>2:
#             raise VaccinationOverdueError("Cat vaccination overdue!")
#         print("succesfully scheduled")

# pets=[
#     (Dog(),3),
#     (cat(),1)
# ]
# for pet, years in pets:
#     try:
#                 pet.schedule_appointment(years)
#     except VaccinationOverdueError:
#         print("⚠️ Vaccination overdue! Marking appointment as HIGH PRIORITY.\n")

#Q35A university campus manages automated vending machines. Create a base 
# class VendingMachine with a method dispense_item(). Derive SnackMachine and DrinkMachine. 
# Through polymorphism, the Snack machine drops items via coils, while the Drink 
# machine utilizes a robotic arm. Implement a custom ItemStuckError. If infrared sensors 
# don't detect an item dropping within 5 seconds of dispensing, raise the exception, catch 
# it, and automatically refund the user's digital wallet.

class ItemStuckError(Exception):
  pass
class VendingMachine :
  def dispense_item(self,time):
    print("Dispensing item..")

class SnackMachine(VendingMachine):
  def dispense_item(self,time):
    print(" drops items via coils")
    if time:
      raise ItemStuckError("infrared sensors don't detect an item dropping within 5 seconds of dispensing")
    print("")
class DrinkMachine(VendingMachine):
  def dispense_item(self,time):
    print("  utilizes a robotic arm")
    if time>5:
      raise ItemStuckError("infrared sensors don't detect an item dropping within 5 seconds of dispensing")
    print("")

    machines=[
      ((SnackMachine),7),
      ((DrinkMachine),3)
    ]
   
for machine, status in machines:
    try:
        machine.dispense_item(status)
    except ItemStuckError:
        print("⚠️ Item not detected within 5 seconds.")
        print("💰 Refunding amount to user's digital wallet.\n")
