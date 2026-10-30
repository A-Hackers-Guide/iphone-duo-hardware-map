# `UISceneConnectionOptions`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 14 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _launchOptionsDictionary;
@"FBSScene" _fbsScene;
@"FBSSceneSpecification" _specification;
@"NSSet" _cleanupBlocks;
@"_UISceneConnectionOptionDefinitionPayloadStorage" _definitionPayloadStorage;
@"BSKeyedSettings" _connectionValues;
```

## Properties

```
@property (T@"NSDictionary",R,C,N,V_launchOptionsDictionary) _launchOptionsDictionary;
@property (T@"FBSScene",R,W,N,V_fbsScene) _fbsScene;
@property (T@"FBSSceneSpecification",R,W,N,V_specification) _specification;
@property (T@"NSSet",R,C,N) _itemProviderCollections;
@property (T@"NSSet",R,C,N) _assistantTasks;
@property (T@"<NSObject>",R,N) _companionUserInfo;
@property (T@"NSSet",R,C,D,N) URLContexts;
@property (T@"NSString",R,D,N) sourceApplication;
@property (T@"NSString",R,D,N) handoffUserActivityType;
@property (T@"NSSet",R,C,D,N) userActivities;
@property (T@"UNNotificationResponse",R,D,N) notificationResponse;
@property (T@"UIApplicationShortcutItem",R,D,N) shortcutItem;
@property (T@"CKShareMetadata",R,D,N) cloudKitShareMetadata;
@property (T@,R,N) sceneAccessoryUserInfo;
```

## Instance methods

```
-[UISceneConnectionOptions userActivities];
-[UISceneConnectionOptions sourceApplication];
-[UISceneConnectionOptions description];
-[UISceneConnectionOptions _assistantTasks];
-[UISceneConnectionOptions URLContexts];
-[UISceneConnectionOptions _companionUserInfo];
-[UISceneConnectionOptions _fbsScene];
-[UISceneConnectionOptions _flagForConnectionValueKey:];
-[UISceneConnectionOptions _itemProviderCollections];
-[UISceneConnectionOptions _launchOptionsDictionary];
-[UISceneConnectionOptions _objectForConnectionValueKey:];
-[UISceneConnectionOptions _specification];
-[UISceneConnectionOptions cloudKitShareMetadata];
-[UISceneConnectionOptions handoffUserActivityType];
-[UISceneConnectionOptions notificationResponse];
-[UISceneConnectionOptions sceneAccessoryUserInfo];
-[UISceneConnectionOptions shortcutItem];
```
