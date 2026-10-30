# `FBSWorkspaceInitializationOptions`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _endpointMonitoringEnabled;
B _defaultShellEndpointEnabled;
@"<FBSWorkspaceDelegate>" _delegate;
@"BSServiceQueue" _callOutQueue;
```

## Properties

```
@property (TB,N,GisEndpointMonitoringEnabled,V_endpointMonitoringEnabled) endpointMonitoringEnabled;
@property (TB,N,GisDefaultShellEndpointEnabled,V_defaultShellEndpointEnabled) defaultShellEndpointEnabled;
@property (T@"<FBSWorkspaceDelegate>",R,N,V_delegate) delegate;
@property (T@"BSServiceQueue",&,N,V_callOutQueue) callOutQueue;
```

## Class methods

```
+[FBSWorkspaceInitializationOptions optionsWithDelegate:];
```

## Instance methods

```
-[FBSWorkspaceInitializationOptions setDefaultShellEndpointEnabled:];
-[FBSWorkspaceInitializationOptions setCallOutQueue:];
-[FBSWorkspaceInitializationOptions callOutQueue];
-[FBSWorkspaceInitializationOptions init];
-[FBSWorkspaceInitializationOptions setValue:forKey:];
-[FBSWorkspaceInitializationOptions setEndpointMonitoringEnabled:];
-[FBSWorkspaceInitializationOptions isDefaultShellEndpointEnabled];
-[FBSWorkspaceInitializationOptions isEndpointMonitoringEnabled];
-[FBSWorkspaceInitializationOptions delegate];
-[FBSWorkspaceInitializationOptions _initWithDelegate:];
```
