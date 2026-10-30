# `CAFSelectableNotificationEntryList`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSFastEnumeration`
- 2 instance variables, 4 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _selectableNotificationEntrys;
@"NSError" _parseError;
```

## Properties

```
@property (T@"NSArray",R,N,V_selectableNotificationEntrys) selectableNotificationEntrys;
@property (T@"NSError",R,N,V_parseError) parseError;
@property (T@"NSString",R,N) formattedValue;
@property (T@"NSArray",R,N) arrayRepresentation;
```

## Class methods

```
+[CAFSelectableNotificationEntryList selectableNotificationEntryListWithArray:];
+[CAFSelectableNotificationEntryList selectableNotificationEntryListWithSelectableNotificationEntrys:];
```

## Instance methods

```
-[CAFSelectableNotificationEntryList formattedValue];
-[CAFSelectableNotificationEntryList objectAtIndexedSubscript:];
-[CAFSelectableNotificationEntryList initWithArray:];
-[CAFSelectableNotificationEntryList countByEnumeratingWithState:objects:count:];
-[CAFSelectableNotificationEntryList arrayRepresentation];
-[CAFSelectableNotificationEntryList objectAtIndex:];
-[CAFSelectableNotificationEntryList parseError];
-[CAFSelectableNotificationEntryList selectableNotificationEntrys];
-[CAFSelectableNotificationEntryList initWithSelectableNotificationEntrys:];
```
