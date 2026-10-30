# `ASAccessoryCompanionAppInfo`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _appIsInstalled;
@"NSString" _bundleID;
@"NSString" _name;
@"NSString" _publisherName;
@"NSString" _adamID;
@"UIImage" _icon;
@"NSString" _distributorBundleID;
@"NSString" _distributorName;
```

## Properties

```
@property (T@"NSString",R,N,V_bundleID) bundleID;
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSString",R,N,V_publisherName) publisherName;
@property (T@"NSString",R,N,V_adamID) adamID;
@property (T@"UIImage",R,N,V_icon) icon;
@property (TB,R,N,V_appIsInstalled) appIsInstalled;
@property (T@"NSString",R,N,V_distributorBundleID) distributorBundleID;
@property (T@"NSString",R,N,V_distributorName) distributorName;
```

## Class methods

```
+[ASAccessoryCompanionAppInfo appInfoWithBundleID:completion:];
```

## Instance methods

```
-[ASAccessoryCompanionAppInfo adamID];
-[ASAccessoryCompanionAppInfo bundleID];
-[ASAccessoryCompanionAppInfo name];
-[ASAccessoryCompanionAppInfo icon];
-[ASAccessoryCompanionAppInfo publisherName];
-[ASAccessoryCompanionAppInfo appIsInstalled];
-[ASAccessoryCompanionAppInfo distributorBundleID];
-[ASAccessoryCompanionAppInfo distributorName];
-[ASAccessoryCompanionAppInfo initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:distributorBundleID:distributorName:];
```
