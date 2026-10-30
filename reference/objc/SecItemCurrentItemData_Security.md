# `SecItemCurrentItemData`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSData" _persistentRef;
@"NSDate" _currentItemPointerModificationTime;
```

## Properties

```
@property (T@"NSData",&,V_persistentRef) persistentRef;
@property (T@"NSDate",&,V_currentItemPointerModificationTime) currentItemPointerModificationTime;
```

## Instance methods

```
-[SecItemCurrentItemData persistentRef];
-[SecItemCurrentItemData initWithPersistentRef:];
-[SecItemCurrentItemData currentItemPointerModificationTime];
-[SecItemCurrentItemData setCurrentItemPointerModificationTime:];
-[SecItemCurrentItemData setPersistentRef:];
```
