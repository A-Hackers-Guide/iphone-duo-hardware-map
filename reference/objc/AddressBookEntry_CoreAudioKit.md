# `AddressBookEntry`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
I _objectID;
@"NSString" _name;
@"NSString" _address;
q _port;
@"NSString" _serviceType;
```

## Properties

```
@property (TI,R,V_objectID) objectID;
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSString",&,N,V_serviceType) serviceType;
@property (T@"NSString",&,N) fullAddress;
@property (T@"NSString",R,V_address) address;
@property (Tq,R,V_port) port;
@property (Ti,R) sessionType;
```

## Instance methods

```
-[AddressBookEntry address];
-[AddressBookEntry setObjectID:];
-[AddressBookEntry initWithDictionary:];
-[AddressBookEntry init];
-[AddressBookEntry objectID];
-[AddressBookEntry port];
-[AddressBookEntry sessionType];
-[AddressBookEntry setName:];
-[AddressBookEntry copyWithZone:];
-[AddressBookEntry setServiceType:];
-[AddressBookEntry name];
-[AddressBookEntry serviceType];
-[AddressBookEntry fullAddress];
-[AddressBookEntry setFullAddress:];
-[AddressBookEntry init:sessionType:fullAddress:];
```
