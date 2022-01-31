DB Schema 


# Post
  * ID - PK INT 
  * author - FK one to many 
  * title str 
  * intro: str 
  * body: text
  * photo_main (main_image): str
  * is_published: bool (default: [true])
  * published date (default now)

# Author 
  * ID - PK INT 
  * name: str 
  * photo: str 
  * description: text
  * email: nullable str 
  * linkedin: nullable str 
  * github: nullable str
