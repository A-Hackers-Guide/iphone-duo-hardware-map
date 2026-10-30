# `NFACTag`

- Image: [`/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory`](../userland/System__Library__PrivateFrameworks__NearFieldAccessory.framework__NearFieldAccessory.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NFACTag`
- 15 instance variables, 13 properties, 25 instance methods, 1 class methods

## Instance variables

```
I _technology;
I _type;
@"NSData" _tagID;
@"NSData" _pmm;
@"NSArray" _allSystemCodes;
@"NSData" _appData;
@"NSData" _uid;
@"NSString" _description;
I _ndefAvailability;
Q _ndefMessageSize;
Q _ndefContainerSize;
@"NSData" _atqa;
@"NSData" _sak;
@"NSData" _historicalBytes;
C _silentType;
```

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
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[NFACTag supportsSecureCoding];
```

## Instance methods

```
-[NFACTag UID];
-[NFACTag asDictionary];
-[NFACTag tagID];
-[NFACTag isSilent];
-[NFACTag type];
-[NFACTag encodeWithCoder:];
-[NFACTag description];
-[NFACTag initWithCoder:];
-[NFACTag technology];
-[NFACTag applicationData];
-[NFACTag ndefMessageSize];
-[NFACTag ndefAvailability];
-[NFACTag ndefContainerSize];
-[NFACTag PMm];
-[NFACTag IDm];
-[NFACTag SystemCode];
-[NFACTag selectedAID];
-[NFACTag historicalBytes];
-[NFACTag sak];
-[NFACTag allSystemCodes];
-[NFACTag applicationDataCoding];
-[NFACTag atqa];
-[NFACTag pupi];
-[NFACTag silentType];
-[NFACTag initWithInternalTag:];
```
