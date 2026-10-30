# `FBSystemServiceOpenApplicationRequest`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSString" _bundleIdentifier;
@"FBSOpenApplicationOptions" _options;
@"FBProcess" _clientProcess;
B _trusted;
```

## Properties

```
@property (TB,N,GisTrusted,V_trusted) trusted;
@property (T@"NSString",C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"FBSOpenApplicationOptions",C,N,V_options) options;
@property (T@"FBProcess",&,N,V_clientProcess) clientProcess;
```

## Instance methods

```
-[FBSystemServiceOpenApplicationRequest clientProcess];
-[FBSystemServiceOpenApplicationRequest setOptions:];
-[FBSystemServiceOpenApplicationRequest bundleIdentifier];
-[FBSystemServiceOpenApplicationRequest setClientProcess:];
-[FBSystemServiceOpenApplicationRequest initWithBundleId:];
-[FBSystemServiceOpenApplicationRequest description];
-[FBSystemServiceOpenApplicationRequest options];
-[FBSystemServiceOpenApplicationRequest setBundleIdentifier:];
-[FBSystemServiceOpenApplicationRequest setTrusted:];
-[FBSystemServiceOpenApplicationRequest isTrusted];
```
