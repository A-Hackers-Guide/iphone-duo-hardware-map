# `CAFMediaItem`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 15 properties, 18 instance methods, 0 class methods

## Instance variables

```
C _mediaItemCategory;
C _multicast;
I _frequency;
@"NSString" _artist;
@"NSString" _ensemble;
@"NSString" _identifier;
@"NSString" _mediaItemCategoryUserVisibleLabel;
@"NSString" _mediaItemGroup;
@"NSString" _mediaItemImageIdentifier;
@"NSString" _mediaItemName;
@"NSString" _mediaItemShortName;
@"NSString" _mediaItemType;
@"NSString" _title;
@"NSString" _userVisibleDescription;
```

## Properties

```
@property (T@"NSString",R,C,N,V_artist) artist;
@property (T@"NSString",R,C,N,V_ensemble) ensemble;
@property (TI,R,N,V_frequency) frequency;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (TC,R,N,V_mediaItemCategory) mediaItemCategory;
@property (T@"NSString",R,C,N,V_mediaItemCategoryUserVisibleLabel) mediaItemCategoryUserVisibleLabel;
@property (T@"NSString",R,C,N,V_mediaItemGroup) mediaItemGroup;
@property (T@"NSString",R,C,N,V_mediaItemImageIdentifier) mediaItemImageIdentifier;
@property (T@"NSString",R,C,N,V_mediaItemName) mediaItemName;
@property (T@"NSString",R,C,N,V_mediaItemShortName) mediaItemShortName;
@property (T@"NSString",R,C,N,V_mediaItemType) mediaItemType;
@property (TC,R,N,V_multicast) multicast;
@property (T@"NSString",R,C,N,V_title) title;
@property (T@"NSString",R,C,N,V_userVisibleDescription) userVisibleDescription;
@property (T@"NSDictionary",R,N) dictionaryRepresentation;
```

## Instance methods

```
-[CAFMediaItem frequency];
-[CAFMediaItem initWithDictionary:];
-[CAFMediaItem identifier];
-[CAFMediaItem artist];
-[CAFMediaItem title];
-[CAFMediaItem description];
-[CAFMediaItem dictionaryRepresentation];
-[CAFMediaItem multicast];
-[CAFMediaItem mediaItemType];
-[CAFMediaItem ensemble];
-[CAFMediaItem mediaItemName];
-[CAFMediaItem mediaItemShortName];
-[CAFMediaItem userVisibleDescription];
-[CAFMediaItem initWithArtist:ensemble:frequency:identifier:mediaItemCategory:mediaItemCategoryUserVisibleLabel:mediaItemGroup:mediaItemImageIdentifier:mediaItemName:mediaItemShortName:mediaItemType:multicast:title:userVisibleDescription:];
-[CAFMediaItem mediaItemCategory];
-[CAFMediaItem mediaItemCategoryUserVisibleLabel];
-[CAFMediaItem mediaItemGroup];
-[CAFMediaItem mediaItemImageIdentifier];
```
