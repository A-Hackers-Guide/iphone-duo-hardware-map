# `_ACPluginDB`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 0 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"NSMutableDictionary" mSearchDirectories;
B mDirty;
@"NSObject<OS_dispatch_queue>" mDispatchQueue;
{function<void (AudioComponentVector &, AudioComponentVector &)>="__f_"{__value_func<void (AudioComponentVector &, AudioComponentVector &)>="__buf_"(type="__data"[24C])"__f_"^v}} mNotificationCallback;
{function<void ()>="__f_"{__value_func<void ()>="__buf_"(type="__data"[24C])"__f_"^v}} mScanHashCallback;
@"NSData" mCarbonComponentHash;
```

## Class methods

```
+[_ACPluginDB supportsSecureCoding];
+[_ACPluginDB path];
```

## Instance methods

```
-[_ACPluginDB init];
-[_ACPluginDB encodeWithCoder:];
-[_ACPluginDB initWithCoder:];
-[_ACPluginDB initialScanDirectory:priority:components:];
-[_ACPluginDB postInit:];
-[_ACPluginDB writeIfDirty];
```
