# `_ACPluginDBBundle`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSString" mFullPath;
d mInfoPlistModDate;
d mRsrcModDate;
{AudioComponentVector="__begin_"^v"__end_"^v""{?="__cap_"^v}"mSorted"B} mBundleComponentVector;
```

## Class methods

```
+[_ACPluginDBBundle supportsSecureCoding];
```

## Instance methods

```
-[_ACPluginDBBundle encodeWithCoder:];
-[_ACPluginDBBundle initWithCoder:];
-[_ACPluginDBBundle initWithPath:infoPlistModDate:rsrcModDate:];
-[_ACPluginDBBundle loadAllComponents:];
-[_ACPluginDBBundle scanWithPriority:loadable:infoPlistPath:];
```
