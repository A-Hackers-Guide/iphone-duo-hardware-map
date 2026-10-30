# `MTLIOAccelResourcePool`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
{_MTLIOAccelResourcePoolPrivate="volatileQueue"{_MTLIOAccelResourceQueue="tqh_first"@"MTLIOAccelPooledResource""tqh_last"^@}"nonvolatileQueue"{_MTLIOAccelResourceQueue="tqh_first"@"MTLIOAccelPooledResource""tqh_last"^@}"lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"count"i} _priv;
# _resourceClass;
@"MTLIOAccelDevice<MTLDevice>" _device;
^{IOAccelNewResourceArgs={IOAccelNewResourceData=IISSSSQQCCCCIQQQ(?={?=QQQQI}{?=II[3Q]}{?=IIII[2Q]}{?=II[3Q]})}} _resourceArgs;
I _resourceArgsSize;
Q age_to_purge;
I generation;
```

## Properties

```
@property (T^{IOAccelNewResourceArgs={IOAccelNewResourceData=IISSSSQQCCCCIQQQ(?={?=QQQQI}{?=II[3Q]}{?=IIII[2Q]}{?=II[3Q]})}},R,V_resourceArgs) resourceArgs;
@property (TI,R,V_resourceArgsSize) resourceArgsSize;
```

## Instance methods

```
-[MTLIOAccelResourcePool availableCount];
-[MTLIOAccelResourcePool initWithDevice:resourceClass:resourceArgs:resourceArgsSize:options:];
-[MTLIOAccelResourcePool dealloc];
-[MTLIOAccelResourcePool setResourceArgs:resourceArgsSize:];
-[MTLIOAccelResourcePool purgeWithLock];
-[MTLIOAccelResourcePool purge];
-[MTLIOAccelResourcePool resourceArgsSize];
-[MTLIOAccelResourcePool resourceArgs];
-[MTLIOAccelResourcePool updateResourcePurgeability];
```
