# `AudioComponentPrefRegConnection`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AudioComponentPreferenceProtocol`
- 2 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
^v mImpl;
{ConnectionInfo="mConnection"@"NSXPCConnection""mExtUsePermission"i"mLinkedSDKRequiresEntitlement"B} mConnInfo;
```

## Instance methods

```
-[AudioComponentPrefRegConnection clearConfigurationInfoCache:];
-[AudioComponentPrefRegConnection copyConfigurationInfoFromCache:reply:];
-[AudioComponentPrefRegConnection getComponentUserTags:reply:];
-[AudioComponentPrefRegConnection getExtensionComponentList:linkedSDKRequiresEntitlement:reply:];
-[AudioComponentPrefRegConnection getExtensionIcon:reply:];
-[AudioComponentPrefRegConnection getInterAppIcon:reply:];
-[AudioComponentPrefRegConnection initWithRegistrar:connection:];
-[AudioComponentPrefRegConnection isGenericAppIcon:size:scale:];
-[AudioComponentPrefRegConnection setComponentUserTags:tags:];
-[AudioComponentPrefRegConnection setExtensionComponentList:linkedSDKRequiresEntitlement:components:reply:];
-[AudioComponentPrefRegConnection writeConfigurationInfoToCache:configurationInfo:];
```
