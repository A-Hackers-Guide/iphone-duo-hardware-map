# `SRSampleViewController`

- Image: [`/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI`](../userland/System__Library__PrivateFrameworks__SensorKitUI.framework__SensorKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewController`
- 3 instance variables, 3 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _sampleDataEntries;
@"NSString" _note;
@"SRAuthorizationGroup" _authGroup;
```

## Properties

```
@property (T@"NSArray",&,N,V_sampleDataEntries) sampleDataEntries;
@property (T@"NSString",&,N,V_note) note;
@property (T@"SRAuthorizationGroup",&,N,V_authGroup) authGroup;
```

## Class methods

```
+[SRSampleViewController initialize];
+[SRSampleViewController sampleViewControllerForAuthGroup:];
```

## Instance methods

```
-[SRSampleViewController tableView:titleForFooterInSection:];
-[SRSampleViewController tableView:numberOfRowsInSection:];
-[SRSampleViewController numberOfSectionsInTableView:];
-[SRSampleViewController tableView:cellForRowAtIndexPath:];
-[SRSampleViewController init];
-[SRSampleViewController dealloc];
-[SRSampleViewController note];
-[SRSampleViewController tableView:didSelectRowAtIndexPath:];
-[SRSampleViewController setNote:];
-[SRSampleViewController authGroup];
-[SRSampleViewController prepareEndRowWithText:detailText:];
-[SRSampleViewController prepareExtendedRowWithText:];
-[SRSampleViewController sampleDataEntries];
-[SRSampleViewController setAuthGroup:];
-[SRSampleViewController setSampleDataEntries:];
-[SRSampleViewController sortedKeysForDictionary:];
```
