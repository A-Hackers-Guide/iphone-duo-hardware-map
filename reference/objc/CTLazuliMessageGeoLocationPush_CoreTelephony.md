# `CTLazuliMessageGeoLocationPush`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"CTLazuliLocationCoordinates" _coordinates;
@"NSString" _additionalDescription;
@"CTLazuliChatBotSuggestedChipList" _chipList;
@"CTLazuliCustomMetaData" _metaData;
```

## Properties

```
@property (T@"CTLazuliChatBotSuggestedChipList",&,N,V_chipList) chipList;
@property (T@"CTLazuliLocationCoordinates",&,N,V_coordinates) coordinates;
@property (T@"NSString",&,N,V_additionalDescription) additionalDescription;
@property (T@"CTLazuliCustomMetaData",&,N,V_metaData) metaData;
```

## Class methods

```
+[CTLazuliMessageGeoLocationPush supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliMessageGeoLocationPush setMetaData:];
-[CTLazuliMessageGeoLocationPush metaData];
-[CTLazuliMessageGeoLocationPush additionalDescription];
-[CTLazuliMessageGeoLocationPush encodeWithCoder:];
-[CTLazuliMessageGeoLocationPush description];
-[CTLazuliMessageGeoLocationPush initWithCoder:];
-[CTLazuliMessageGeoLocationPush copyWithZone:];
-[CTLazuliMessageGeoLocationPush isEqual:];
-[CTLazuliMessageGeoLocationPush chipList];
-[CTLazuliMessageGeoLocationPush setCoordinates:];
-[CTLazuliMessageGeoLocationPush coordinates];
-[CTLazuliMessageGeoLocationPush initWithReflection:];
-[CTLazuliMessageGeoLocationPush isEqualToCTLazuliMessageGeoLocationPush:];
-[CTLazuliMessageGeoLocationPush setAdditionalDescription:];
-[CTLazuliMessageGeoLocationPush setChipList:];
```
