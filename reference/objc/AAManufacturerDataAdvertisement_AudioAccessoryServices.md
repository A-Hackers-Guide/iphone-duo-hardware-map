# `AAManufacturerDataAdvertisement`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
S _companyID;
@"NSData" _manufacturerData;
@"NSArray" _payloads;
```

## Properties

```
@property (TS,R,V_companyID) companyID;
@property (T@"NSData",R,N,V_manufacturerData) manufacturerData;
@property (T@"NSArray",R,N,V_payloads) payloads;
```

## Class methods

```
+[AAManufacturerDataAdvertisement manufacturerDataWithData:];
```

## Instance methods

```
-[AAManufacturerDataAdvertisement payloads];
-[AAManufacturerDataAdvertisement hash];
-[AAManufacturerDataAdvertisement initWithData:];
-[AAManufacturerDataAdvertisement isEqual:];
-[AAManufacturerDataAdvertisement manufacturerData];
-[AAManufacturerDataAdvertisement companyID];
-[AAManufacturerDataAdvertisement _parsePayloads];
-[AAManufacturerDataAdvertisement isEqualToAdvertisement:];
```
