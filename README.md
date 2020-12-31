/// File-based-key-value-pair-with-crd-operation ///

File-based key-value data store that supports the basic CRD (create, read, and delete) operations with multi-threading and time-to-live property.
This data store is meant to be used as a local storage for 1 single process on one LaptopThe data store must be exposed as a library to clients that can instantiate a class and work with the data store.

The data will be stored on the crd.txt file which can be accessed in the folder.
