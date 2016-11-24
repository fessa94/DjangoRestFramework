Overview - I decided to pick Shisha for my domain, Shisha is the name given to an Arabian water pipe. The API that I have developed allows for a small shisha lounge to manage stock.
Models - After analyzing the needs of a shisha lounge, I developed 3 separate models, which are shisha, Manufacturer and Vendor. The reason for having both manufacturer and vendors is because I noticed that most shisha manufacturers are based in the Middle Eastern region and have local vendors. The structure is such that each shisha flavor has a manufacturer and each manufacturer has a vendor.
Serializes - As part of my implementation I developed 3 separate serializes, the role of the serializer is to convert querysets into native python data types so that it can easily be converted into JSON, XML and other data types. In my case I utilized a HyperlinkedModelSerialzer over a ModelSerializer as I preferred using hyperlinks to demonstrate the relationship between my objects.
Model Sets and Routers – I decided to make use of view states over just using straight out views as it enabled me to spend more time on defining my model, as it
provides a greater level of abstraction by providing an inbuilt implementation for operations such as read, update, get and put
