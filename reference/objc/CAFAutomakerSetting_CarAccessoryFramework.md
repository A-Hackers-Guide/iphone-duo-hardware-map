# `CAFAutomakerSetting`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositioned`
- 0 instance variables, 37 properties, 51 instance methods, 0 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) userVisibleLabelCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) sectionIdentifierCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) sortOrderCharacteristic;
@property (T@"CAFSettingsCategoryCharacteristic",R,N) categoryCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) disabledCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) limitableUIElementCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) hiddenCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) showAudioBrandLogoCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) symbolNameCharacteristic;
@property (T@"CAFProminenceInformationCharacteristic",R,N) prominenceInfoCharacteristic;
@property (T@"NSString",R,N) userVisibleLabel;
@property (T@"NSString",R,N) sectionIdentifier;
@property (TB,R,N) hasSectionIdentifier;
@property (TC,R,N) sortOrder;
@property (TB,R,N) hasSortOrder;
@property (TC,R,N) category;
@property (T@"NSString",R,N) identifier;
@property (TB,R,N) disabled;
@property (TB,R,N) hasDisabled;
@property (TB,R,N) limitableUIElement;
@property (TB,R,N) hasLimitableUIElement;
@property (TB,R,N) hidden;
@property (TB,R,N) hasHidden;
@property (TB,R,N) showAudioBrandLogo;
@property (TB,R,N) hasShowAudioBrandLogo;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (TB,R,N) hasVehicleLayoutKey;
@property (T@"NSString",R,N) symbolName;
@property (TB,R,N) hasSymbolName;
@property (T@"CAFProminenceInformation",R,N) prominenceInfo;
@property (TB,R,N) hasProminenceInfo;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAFAutomakerSetting sortOrder];
-[CAFAutomakerSetting disabled];
-[CAFAutomakerSetting identifier];
-[CAFAutomakerSetting removeObserver:];
-[CAFAutomakerSetting category];
-[CAFAutomakerSetting symbolName];
-[CAFAutomakerSetting addObserver:];
-[CAFAutomakerSetting sectionIdentifier];
-[CAFAutomakerSetting registerObserver:];
-[CAFAutomakerSetting hasDisabled];
-[CAFAutomakerSetting name];
-[CAFAutomakerSetting unregisterObserver:];
-[CAFAutomakerSetting hidden];
-[CAFAutomakerSetting hasSortOrder];
-[CAFAutomakerSetting hasSectionIdentifier];
-[CAFAutomakerSetting hasSymbolName];
-[CAFAutomakerSetting hasHidden];
-[CAFAutomakerSetting hasLimitableUIElement];
-[CAFAutomakerSetting hasShowAudioBrandLogo];
-[CAFAutomakerSetting limitableUIElement];
-[CAFAutomakerSetting prominenceInfo];
-[CAFAutomakerSetting registeredForDisabled];
-[CAFAutomakerSetting registeredForHidden];
-[CAFAutomakerSetting registeredForIdentifier];
-[CAFAutomakerSetting registeredForSortOrder];
-[CAFAutomakerSetting registeredForSymbolName];
-[CAFAutomakerSetting registeredForUserVisibleLabel];
-[CAFAutomakerSetting registeredForVehicleLayoutKey];
-[CAFAutomakerSetting showAudioBrandLogo];
-[CAFAutomakerSetting userVisibleLabel];
-[CAFAutomakerSetting vehicleLayoutKey];
-[CAFAutomakerSetting registeredForLimitableUIElement];
-[CAFAutomakerSetting registeredForShowAudioBrandLogo];
-[CAFAutomakerSetting sectionIdentifierCharacteristic];
-[CAFAutomakerSetting _characteristicDidUpdate:fromGroupUpdate:];
-[CAFAutomakerSetting categoryCharacteristic];
-[CAFAutomakerSetting disabledCharacteristic];
-[CAFAutomakerSetting hasProminenceInfo];
-[CAFAutomakerSetting hasVehicleLayoutKey];
-[CAFAutomakerSetting hiddenCharacteristic];
-[CAFAutomakerSetting identifierCharacteristic];
-[CAFAutomakerSetting limitableUIElementCharacteristic];
-[CAFAutomakerSetting prominenceInfoCharacteristic];
-[CAFAutomakerSetting registeredForProminenceInfo];
-[CAFAutomakerSetting registeredForSectionIdentifier];
-[CAFAutomakerSetting registeredForSettingsCategory];
-[CAFAutomakerSetting showAudioBrandLogoCharacteristic];
-[CAFAutomakerSetting sortOrderCharacteristic];
-[CAFAutomakerSetting symbolNameCharacteristic];
-[CAFAutomakerSetting userVisibleLabelCharacteristic];
-[CAFAutomakerSetting vehicleLayoutKeyCharacteristic];
```
