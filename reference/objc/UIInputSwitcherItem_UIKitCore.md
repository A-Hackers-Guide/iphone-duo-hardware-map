# `UIInputSwitcherItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 14 properties, 30 instance methods, 1 class methods

## Instance variables

```
B _usesDeviceLanguage;
@"NSString" _identifier;
@"NSString" _localizedTitle;
@"NSString" _localizedSubtitle;
@"UIFont" _titleFont;
@"UIFont" _subtitleFont;
@"UISwitch" _switchControl;
@? _switchIsOnBlock;
@? _switchToggleBlock;
q _selectedSegmentIndex;
@"NSArray" _segmentTitles;
@"NSArray" _segmentImages;
@? _persistentSelectedIndex;
```

## Properties

```
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_localizedTitle) localizedTitle;
@property (T@"NSString",C,N,V_localizedSubtitle) localizedSubtitle;
@property (T@"UIFont",&,N,V_titleFont) titleFont;
@property (T@"UIFont",&,N,V_subtitleFont) subtitleFont;
@property (TB,N,V_usesDeviceLanguage) usesDeviceLanguage;
@property (T@"UISwitch",&,N,V_switchControl) switchControl;
@property (T@?,C,N,V_switchIsOnBlock) switchIsOnBlock;
@property (T@?,C,N,V_switchToggleBlock) switchToggleBlock;
@property (TB,R,N) isSegmentedItem;
@property (Tq,N,V_selectedSegmentIndex) selectedSegmentIndex;
@property (T@"NSArray",&,N,V_segmentTitles) segmentTitles;
@property (T@"NSArray",&,N,V_segmentImages) segmentImages;
@property (T@?,C,N,V_persistentSelectedIndex) persistentSelectedIndex;
```

## Class methods

```
+[UIInputSwitcherItem switcherItemWithIdentifier:];
```

## Instance methods

```
-[UIInputSwitcherItem localizedTitle];
-[UIInputSwitcherItem identifier];
-[UIInputSwitcherItem dealloc];
-[UIInputSwitcherItem setIdentifier:];
-[UIInputSwitcherItem setLocalizedTitle:];
-[UIInputSwitcherItem titleFont];
-[UIInputSwitcherItem setLocalizedSubtitle:];
-[UIInputSwitcherItem setSwitchControl:];
-[UIInputSwitcherItem localizedSubtitle];
-[UIInputSwitcherItem setTitleFont:];
-[UIInputSwitcherItem initWithIdentifier:];
-[UIInputSwitcherItem isSegmentedItem];
-[UIInputSwitcherItem switchIsOnBlock];
-[UIInputSwitcherItem indexForKeyboardMode:];
-[UIInputSwitcherItem persistentSelectedIndex];
-[UIInputSwitcherItem segmentImages];
-[UIInputSwitcherItem segmentTitles];
-[UIInputSwitcherItem selectedSegmentIndex];
-[UIInputSwitcherItem setPersistentSelectedIndex:];
-[UIInputSwitcherItem setSegmentImages:];
-[UIInputSwitcherItem setSegmentTitles:];
-[UIInputSwitcherItem setSelectedSegmentIndex:];
-[UIInputSwitcherItem setSubtitleFont:];
-[UIInputSwitcherItem setSwitchIsOnBlock:];
-[UIInputSwitcherItem setSwitchToggleBlock:];
-[UIInputSwitcherItem setUsesDeviceLanguage:];
-[UIInputSwitcherItem subtitleFont];
-[UIInputSwitcherItem switchControl];
-[UIInputSwitcherItem switchToggleBlock];
-[UIInputSwitcherItem usesDeviceLanguage];
```
