# `E911LocationSelector`

- Image: [`/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`](../userland/System__Library__PrivateFrameworks__IPTelephony.framework__Support__libIPTelephony.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLEmergencyLocationSelectorDelegate`
- 5 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSBundle" _bundle;
@"CLEmergencyLocationSelector" _location;
@"CLEmergencyLocationSelectorConfig" _config;
{weak_ptr<ImsLocationSelectorDelegate>="__ptr_"^{ImsLocationSelectorDelegate}"__cntrl_"^{__shared_weak_count}} _delegate;
I _confidence;
```

## Instance methods

```
-[E911LocationSelector dealloc];
-[E911LocationSelector locationSelectorDidSelectLocation:];
-[E911LocationSelector initWithDelegate:sipStack:updateMode:dispatchQueue:];
```
