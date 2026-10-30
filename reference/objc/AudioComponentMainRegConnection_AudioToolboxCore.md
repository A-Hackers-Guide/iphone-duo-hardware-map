# `AudioComponentMainRegConnection`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AudioComponentRegistrarProtocol`
- 2 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
^v mImpl;
{ConnectionInfo="mConnection"@"NSXPCConnection""mExtUsePermission"i"mLinkedSDKRequiresEntitlement"B} mConnInfo;
```

## Instance methods

```
-[AudioComponentMainRegConnection canRegisterComponent:reply:];
-[AudioComponentMainRegConnection getComponentList:linkedSDKRequiresEntitlement:includeExtensions:forceWaitForExtensions:reply:];
-[AudioComponentMainRegConnection initWithRegistrar:connection:];
```
