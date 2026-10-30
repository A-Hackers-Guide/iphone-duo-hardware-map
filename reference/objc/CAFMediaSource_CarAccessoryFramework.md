# `CAFMediaSource`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 24 properties, 39 instance methods, 3 class methods

## Properties

```
@property (T@"CAFUInt32Characteristic",R,N) currentFrequencyCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) currentMediaItemIdentifierCharacteristic;
@property (T@"CAFMediaItemsCharacteristic",R,N) mediaItemsCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleLabelCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFMediaSourceSemanticTypeCharacteristic",R,N) mediaSourceSemanticTypeCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) disabledCharacteristic;
@property (T@"CAFMediaItemImagesCharacteristic",R,N) mediaItemImagesCharacteristic;
@property (TI,R,N) currentFrequency;
@property (T@"CAFUInt32Range",R,N) currentFrequencyRange;
@property (TB,R,N) hasCurrentFrequency;
@property (TB,R,N) currentFrequencyInvalid;
@property (T@"NSString",R,N) currentMediaItemIdentifier;
@property (TB,R,N) hasCurrentMediaItemIdentifier;
@property (TB,R,N) currentMediaItemIdentifierInvalid;
@property (T@"CAFMediaItems",R,N) mediaItems;
@property (TB,R,N) hasMediaItems;
@property (T@"NSString",R,N) userVisibleLabel;
@property (TB,R,N) hasUserVisibleLabel;
@property (T@"NSString",R,N) identifier;
@property (TC,R,N) mediaSourceSemanticType;
@property (TB,R,N) disabled;
@property (T@"CAFMediaItemImages",R,N) mediaItemImages;
@property (TB,R,N) hasMediaItemImages;
```

## Class methods

```
+[CAFMediaSource serviceIdentifier];
+[CAFMediaSource observerProtocol];
+[CAFMediaSource typeComparator];
```

## Instance methods

```
-[CAFMediaSource mediaItems];
-[CAFMediaSource disabled];
-[CAFMediaSource identifier];
-[CAFMediaSource removeObserver:];
-[CAFMediaSource addObserver:];
-[CAFMediaSource registerObserver:];
-[CAFMediaSource name];
-[CAFMediaSource unregisterObserver:];
-[CAFMediaSource currentFrequency];
-[CAFMediaSource mediaItemImages];
-[CAFMediaSource currentFrequencyInvalid];
-[CAFMediaSource currentFrequencyRange];
-[CAFMediaSource currentMediaItemIdentifier];
-[CAFMediaSource currentMediaItemIdentifierInvalid];
-[CAFMediaSource hasCurrentFrequency];
-[CAFMediaSource hasCurrentMediaItemIdentifier];
-[CAFMediaSource mediaSourceSemanticType];
-[CAFMediaSource registeredForCurrentFrequency];
-[CAFMediaSource registeredForCurrentMediaItemIdentifier];
-[CAFMediaSource registeredForDisabled];
-[CAFMediaSource registeredForIdentifier];
-[CAFMediaSource registeredForMediaItemImages];
-[CAFMediaSource registeredForMediaItems];
-[CAFMediaSource registeredForMediaSourceSemanticType];
-[CAFMediaSource registeredForUserVisibleLabel];
-[CAFMediaSource userVisibleLabel];
-[CAFMediaSource _characteristicDidUpdate:fromGroupUpdate:];
-[CAFMediaSource currentFrequencyCharacteristic];
-[CAFMediaSource currentMediaItemIdentifierCharacteristic];
-[CAFMediaSource disabledCharacteristic];
-[CAFMediaSource hasMediaItemImages];
-[CAFMediaSource hasMediaItems];
-[CAFMediaSource hasUserVisibleLabel];
-[CAFMediaSource identifierCharacteristic];
-[CAFMediaSource mediaItemImagesCharacteristic];
-[CAFMediaSource mediaItemsCharacteristic];
-[CAFMediaSource mediaSourceSemanticTypeCharacteristic];
-[CAFMediaSource typeCompare:];
-[CAFMediaSource userVisibleLabelCharacteristic];
```
