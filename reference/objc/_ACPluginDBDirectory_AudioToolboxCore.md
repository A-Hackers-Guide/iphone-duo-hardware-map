# `_ACPluginDBDirectory`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 12 instance variables, 0 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"_ACPluginDB" mDB;
@"NSString" mFullPath;
d mModificationDate;
i mPriority;
@"NSMutableDictionary" mBundlesByName;
^{__FSEventStream=} mFSMonitor;
d mCurrentModificationDate;
@"NSData" mCarbonComponentHash;
B mComponentsLoadable;
@"NSMutableArray" mChangedBundlePaths;
Q mNrOfPathsChanged;
B mShouldRescan;
```

## Class methods

```
+[_ACPluginDBDirectory supportsSecureCoding];
```

## Instance methods

```
-[_ACPluginDBDirectory dealloc];
-[_ACPluginDBDirectory encodeWithCoder:];
-[_ACPluginDBDirectory initWithCoder:];
-[_ACPluginDBDirectory bundlesChanged:shouldRescan:];
-[_ACPluginDBDirectory eventStreamCallback:flags:];
-[_ACPluginDBDirectory initWithPath:priority:];
-[_ACPluginDBDirectory loadAllComponents:];
-[_ACPluginDBDirectory monitorDirectory];
-[_ACPluginDBDirectory refreshModificationDate];
-[_ACPluginDBDirectory scanBundle:loadable:];
-[_ACPluginDBDirectory scanDirectory];
```
