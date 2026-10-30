# `ULBGSystemTaskRequest`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _resourceIntensive;
B _requiresBuddyComplete;
B _requiresUserInactivity;
B _postInstall;
B _requiresExternalPower;
@"NSString" _identifier;
q _priority;
q _requiresProtectionClass;
q _resources;
```

## Properties

```
@property (T@"NSString",&,N,V_identifier) identifier;
@property (Tq,N,V_priority) priority;
@property (Tq,N,V_requiresProtectionClass) requiresProtectionClass;
@property (TB,N,V_resourceIntensive) resourceIntensive;
@property (Tq,N,V_resources) resources;
@property (TB,N,V_requiresBuddyComplete) requiresBuddyComplete;
@property (TB,N,V_requiresUserInactivity) requiresUserInactivity;
@property (TB,N,V_postInstall) postInstall;
@property (TB,N,V_requiresExternalPower) requiresExternalPower;
```

## Instance methods

```
-[ULBGSystemTaskRequest requiresBuddyComplete];
-[ULBGSystemTaskRequest postInstall];
-[ULBGSystemTaskRequest setPostInstall:];
-[ULBGSystemTaskRequest priority];
-[ULBGSystemTaskRequest setRequiresExternalPower:];
-[ULBGSystemTaskRequest resourceIntensive];
-[ULBGSystemTaskRequest identifier];
-[ULBGSystemTaskRequest setPriority:];
-[ULBGSystemTaskRequest requiresExternalPower];
-[ULBGSystemTaskRequest requiresUserInactivity];
-[ULBGSystemTaskRequest setIdentifier:];
-[ULBGSystemTaskRequest resources];
-[ULBGSystemTaskRequest setResourceIntensive:];
-[ULBGSystemTaskRequest setResources:];
-[ULBGSystemTaskRequest setRequiresBuddyComplete:];
-[ULBGSystemTaskRequest requiresProtectionClass];
-[ULBGSystemTaskRequest createRequestFromSelf];
-[ULBGSystemTaskRequest setRequiresProtectionClass:];
-[ULBGSystemTaskRequest initWithIdentifier:];
-[ULBGSystemTaskRequest setRequiresUserInactivity:];
```
