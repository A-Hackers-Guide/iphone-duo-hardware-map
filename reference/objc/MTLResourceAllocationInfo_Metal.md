# `MTLResourceAllocationInfo`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSCoding`
- 0 instance variables, 7 properties, 3 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,D) memoryPool;
@property (TQ,R,D) virtualSize;
@property (TQ,R,D) residentSize;
@property (TQ,R,D) dirtySize;
@property (TB,R,D) pageoffRequired;
@property (TB,R,D) purgeable;
@property (TQ,R,D) uniqueIdentifier;
```

## Instance methods

```
-[MTLResourceAllocationInfo encodeWithCoder:];
-[MTLResourceAllocationInfo initWithCoder:];
-[MTLResourceAllocationInfo copyWithZone:];
```
