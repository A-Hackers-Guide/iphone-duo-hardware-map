# `WFIPViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFInsetTableViewController`
- Protocols: `UITableViewDelegate`, `UITableViewDataSource`
- 3 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _addresses;
@"NSArray" _prefixes;
@"WFAppearanceProxy" _appearanceProxy;
```

## Properties

```
@property (T@"NSArray",&,N,V_addresses) addresses;
@property (T@"NSArray",&,N,V_prefixes) prefixes;
@property (T@"WFAppearanceProxy",&,N,V_appearanceProxy) appearanceProxy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFIPViewController tableView:numberOfRowsInSection:];
-[WFIPViewController numberOfSectionsInTableView:];
-[WFIPViewController tableView:cellForRowAtIndexPath:];
-[WFIPViewController viewDidLoad];
-[WFIPViewController appearanceProxy];
-[WFIPViewController addresses];
-[WFIPViewController setAddresses:];
-[WFIPViewController prefixes];
-[WFIPViewController setPrefixes:];
-[WFIPViewController setAppearanceProxy:];
-[WFIPViewController initWithAddresses:prefixLengths:];
-[WFIPViewController initWithAddresses:prefixLengths:appearanceProxy:];
```
