# `CAFCameraButton`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 28 properties, 46 instance methods, 2 class methods

## Properties

```
@property (T@"CAFButtonActionCharacteristic",R,N) buttonActionCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) contentURLActionCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) sortOrderCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) symbolNameCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) disabledCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) selectedCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) hiddenCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFArrayCharacteristic",R,N) childrenIdentifiersCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) selectedEntryIndexCharacteristic;
@property (TC,N) buttonAction;
@property (TB,R,N) hasButtonAction;
@property (T@"NSString",R,N) contentURLAction;
@property (TB,R,N) hasContentURLAction;
@property (TC,R,N) sortOrder;
@property (T@"NSString",R,N) symbolName;
@property (TB,R,N) disabled;
@property (TB,R,N) hasDisabled;
@property (TB,R,N) selected;
@property (TB,R,N) hasSelected;
@property (TB,R,N) hidden;
@property (TB,R,N) hasHidden;
@property (T@"NSString",R,N) identifier;
@property (T@"NSArray",R,N) childrenIdentifiers;
@property (TB,R,N) hasChildrenIdentifiers;
@property (TC,N) selectedEntryIndex;
@property (T@"CAFUInt8Range",R,N) selectedEntryIndexRange;
@property (TB,R,N) hasSelectedEntryIndex;
```

## Class methods

```
+[CAFCameraButton serviceIdentifier];
+[CAFCameraButton observerProtocol];
```

## Instance methods

```
-[CAFCameraButton sortOrder];
-[CAFCameraButton disabled];
-[CAFCameraButton identifier];
-[CAFCameraButton removeObserver:];
-[CAFCameraButton symbolName];
-[CAFCameraButton addObserver:];
-[CAFCameraButton registerObserver:];
-[CAFCameraButton hasDisabled];
-[CAFCameraButton selected];
-[CAFCameraButton name];
-[CAFCameraButton unregisterObserver:];
-[CAFCameraButton hidden];
-[CAFCameraButton buttonAction];
-[CAFCameraButton setButtonAction:];
-[CAFCameraButton hasButtonAction];
-[CAFCameraButton hasSelected];
-[CAFCameraButton hasHidden];
-[CAFCameraButton childrenIdentifiers];
-[CAFCameraButton registeredForSelectedEntryIndex];
-[CAFCameraButton contentURLAction];
-[CAFCameraButton hasSelectedEntryIndex];
-[CAFCameraButton registeredForButtonAction];
-[CAFCameraButton registeredForChildrenIdentifiers];
-[CAFCameraButton registeredForContentURLAction];
-[CAFCameraButton registeredForDisabled];
-[CAFCameraButton registeredForHidden];
-[CAFCameraButton registeredForIdentifier];
-[CAFCameraButton registeredForSelected];
-[CAFCameraButton registeredForSortOrder];
-[CAFCameraButton registeredForSymbolName];
-[CAFCameraButton selectedEntryIndex];
-[CAFCameraButton setSelectedEntryIndex:];
-[CAFCameraButton _characteristicDidUpdate:fromGroupUpdate:];
-[CAFCameraButton buttonActionCharacteristic];
-[CAFCameraButton childrenIdentifiersCharacteristic];
-[CAFCameraButton contentURLActionCharacteristic];
-[CAFCameraButton disabledCharacteristic];
-[CAFCameraButton hasChildrenIdentifiers];
-[CAFCameraButton hasContentURLAction];
-[CAFCameraButton hiddenCharacteristic];
-[CAFCameraButton identifierCharacteristic];
-[CAFCameraButton selectedCharacteristic];
-[CAFCameraButton selectedEntryIndexCharacteristic];
-[CAFCameraButton selectedEntryIndexRange];
-[CAFCameraButton sortOrderCharacteristic];
-[CAFCameraButton symbolNameCharacteristic];
```
