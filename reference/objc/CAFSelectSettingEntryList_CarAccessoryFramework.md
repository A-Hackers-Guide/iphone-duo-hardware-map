# `CAFSelectSettingEntryList`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSFastEnumeration`
- 2 instance variables, 4 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _selectSettingEntrys;
@"NSError" _parseError;
```

## Properties

```
@property (T@"NSArray",R,N,V_selectSettingEntrys) selectSettingEntrys;
@property (T@"NSError",R,N,V_parseError) parseError;
@property (T@"NSString",R,N) formattedValue;
@property (T@"NSArray",R,N) arrayRepresentation;
```

## Class methods

```
+[CAFSelectSettingEntryList selectSettingEntryListWithArray:];
+[CAFSelectSettingEntryList selectSettingEntryListWithSelectSettingEntrys:];
```

## Instance methods

```
-[CAFSelectSettingEntryList formattedValue];
-[CAFSelectSettingEntryList objectAtIndexedSubscript:];
-[CAFSelectSettingEntryList initWithArray:];
-[CAFSelectSettingEntryList countByEnumeratingWithState:objects:count:];
-[CAFSelectSettingEntryList arrayRepresentation];
-[CAFSelectSettingEntryList objectAtIndex:];
-[CAFSelectSettingEntryList parseError];
-[CAFSelectSettingEntryList selectSettingEntrys];
-[CAFSelectSettingEntryList initWithSelectSettingEntrys:];
```
