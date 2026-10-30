# `IOKRegistryEntry`

- Image: [`/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten`](../userland/System__Library__PrivateFrameworks__IOKitten.framework__IOKitten.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOKObject`
- 0 instance variables, 3 properties, 31 instance methods, 3 class methods

## Properties

```
@property (T@"NSString",R,C,N) name;
@property (TQ,R,N) entryID;
@property (T@"NSDictionary",C,N) properties;
```

## Class methods

```
+[IOKRegistryEntry rootEntry];
+[IOKRegistryEntry entryFromPath:];
+[IOKRegistryEntry registryIteratorForPlane:withOptions:error:];
```

## Instance methods

```
-[IOKRegistryEntry propertyForKey:];
-[IOKRegistryEntry setProperty:forKey:];
-[IOKRegistryEntry properties];
-[IOKRegistryEntry setProperties:];
-[IOKRegistryEntry entryID];
-[IOKRegistryEntry name];
-[IOKRegistryEntry childIteratorInServicePlaneWithError:];
-[IOKRegistryEntry parentIteratorInServicePlaneWithError:];
-[IOKRegistryEntry initWithIOObject:];
-[IOKRegistryEntry childInPlane:error:];
-[IOKRegistryEntry childInServicePlaneWithError:];
-[IOKRegistryEntry childIteratorInPlane:error:];
-[IOKRegistryEntry childIteratorInPlane:error:withEnumerationBlock:];
-[IOKRegistryEntry childIteratorInServicePlaneWithError:enumerationBlock:];
-[IOKRegistryEntry initWithRegistryEntry:];
-[IOKRegistryEntry isAttachedToPlane:];
-[IOKRegistryEntry locationInPlane:error:];
-[IOKRegistryEntry locationInServicePlaneWithError:];
-[IOKRegistryEntry nameInPlane:error:];
-[IOKRegistryEntry nameInServicePlaneWithError:];
-[IOKRegistryEntry parentEntryInPlane:error:];
-[IOKRegistryEntry parentEntryInServicePlaneWithError:];
-[IOKRegistryEntry parentIteratorInPlane:error:];
-[IOKRegistryEntry parentIteratorInPlane:error:withEnumerationBlock:];
-[IOKRegistryEntry parentIteratorInServicePlaneWithError:enumerationBlock:];
-[IOKRegistryEntry pathInPlane:];
-[IOKRegistryEntry pathInServicePlane];
-[IOKRegistryEntry registryIteratorForPlane:withOptions:error:];
-[IOKRegistryEntry registryIteratorForServicePlaneWithOptions:error:];
-[IOKRegistryEntry searchForPropertyWithKey:inPlane:];
-[IOKRegistryEntry searchForPropertyWithKey:inPlane:withOptions:];
```
