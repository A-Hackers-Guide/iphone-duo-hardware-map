# `NFACTag` (protocol)

- Image: [`/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory`](../userland/System__Library__PrivateFrameworks__NearFieldAccessory.framework__NearFieldAccessory.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 9 properties, 11 instance methods, 0 class methods

## Properties

```
@property (TI,R,N) type;
@property (TI,R,N) technology;
@property (TB,R,N) isSilent;
@property (TC,R,N) silentType;
@property (T@"NSData",R,C,N) tagID;
@property (T@"NSData",R,C,N) UID;
@property (TI,R,N) ndefAvailability;
@property (TQ,R,N) ndefMessageSize;
@property (TQ,R,N) ndefContainerSize;
```

## Instance methods

```
-[NFACTag UID];
-[NFACTag asDictionary];
-[NFACTag tagID];
-[NFACTag isSilent];
-[NFACTag type];
-[NFACTag description];
-[NFACTag technology];
-[NFACTag ndefMessageSize];
-[NFACTag ndefAvailability];
-[NFACTag ndefContainerSize];
-[NFACTag silentType];
```
