# `/usr/lib/libsqlite3.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 2,047,680 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 2408)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (2)

- `/usr/lib/libsqlite3.dylib (compatibility version 9.0.0, current version 408.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (2,410)

```
memory
<Unknown>
;
BUG IN CLIENT OF libsqlite3.dylib: illegal multi-threaded access to database connection
Page %u: pointer map referenced
naturaleftouterightfullinnercross
fast
perl
PM
CREATE TABLE x(%s %Q HIDDEN, docid HIDDEN, %Q HIDDEN)
ing
wrong number of vtable arguments
wrong number of arguments to function rtreecheck()
SELECT 1 FROM \"%w\".sqlite_master WHERE name NOT LIKE 'sqliteX_%%' ESCAPE 'X' AND sql NOT LIKE 'create virtual%%' AND sqlite_rename_test(%Q, sql, type, name, %d, %Q, %d)=NULL 
quote
unicode61
SELECT ? UNION SELECT level / (1024 * ?) FROM %Q.'%q_segdir'
fts5: column queries are not supported (detail=none)
hght
more than one 'columns' parameter
UPDATE sqlite_temp_schema SET sql = sqlite_rename_table(%Q, type, name, sql, %Q, %Q, 1), tbl_name = CASE WHEN tbl_name=%Q COLLATE nocase AND   sqlite_rename_test(%Q, sql, type, name, 1, 'after rename', 0) THEN %Q ELSE tbl_name END WHERE typ
40f-20a-20d
%z%.*s
un
Le
ResetSorter
size
SQLITE_ENABLE_LOGGING
%02d:%02d
ROLLBACK; -- due to errors\n
Cannot add a column with non-constant default
jsonb_replace
SELECT t.%Q FROM %Q.%Q AS t WHERE t.%Q MATCH '*id'
ResultRow
compile_options
query_only
randomblob
,origin
UPDATE \"%w\".\"%w_rowid\"SET 
webdav
fchmod
sqlite_altertab_%s
cosh
json_%s() needs an odd number of arguments
SELECT idx, start_block, leaves_end_block, end_block, root FROM %Q.'%q_segdir' WHERE level = ? AND idx = ?
malformed columnsize=... directive
'rebuild' may not be used with a contentless fts5 table
String
IntegrityCk
GROUP
CREATE BLOOM FILTER
*** in database %s ***\n
snippet
fts5_source_id
SQLITE_FORCE_PROXY_LOCKING
TEMP_STORE=1
busy
MULTI-INDEX OR
langid
drop constraint
key
object
HAVING clause on a non-aggregate query
syntax error after column name \"%.*s\"
INSERT OR REPLACE INTO '%q'.'%q_rowid' VALUES(?1, ?2)
MAX_TRIGGER_DEPTH=1000
add column
%s%s
sqlite_temp_schema
SELECT stat FROM %Q.sqlite_stat1 WHERE tbl = '%q_rowid'
)
0
too many levels of trigger recursion
int64
not a writable directory
docid INTEGER PRIMARY KEY
'
date
jsonb_set
SELECT'INSERT INTO %s.'||quote(name)||' SELECT*FROM\"%w\".'||quote(name)FROM %s.sqlite_schema WHERE type='table'AND coalesce(rootpage,1)>0
no such index: \"%s\"
ifnull
json_patch
ize
/usr/tmp
Rewind
CHECK constraints
%s.%s
Vacuum
IfNoHope
number of columns in foreign key does not match the number of columns in the referenced table
SELECT sqlite_fail('constraint %q already exists', %d) FROM \"%w\".sqlite_master WHERE type='table' AND tbl_name=%Q COLLATE nocase AND sqlite_find_constraint(sql, %Q)
->
DELETE FROM %Q.'%q_stat'
IdxGT
eli
pread('%s') failed returning %ld bytes with errno %d
PRAGMA integrity_check
unixShmMap-stat
out of
non-text filename
parse error in rank function: %s
DELETE FROM main.sqlite_stat1 WHERE tbl=?1 AND idx IS CASE WHEN length(?2)=0 AND typeof(?2)='blob' THEN NULL ELSE ?2 END AND (?4 OR stat IS ?3)
/Accounts/Accounts3.sqlite
drop column
the \".\" operator
 USING INTEGER PRIMARY KEY (%s
UPDATE
geteuid
1
table-function argument
SELECT %s WHERE rowid BETWEEN %lld AND %lld ORDER BY rowid %s
pcx
fts5: 2026-04-09 12:25:13 8fa8248e303219400c646a885e36dfc52eae33d83f4412e3f369b2be53737732
Set a breakpoint in sqlite3MutexMisuseAssert to debug
%s: %s
FILTER may not be used with non-aggregate %#T()
too many references to \"%s\": max 65535
BEFORE
insert
CREATE TABLE x(term, col, documents, occurrences, languageid HIDDEN)
NOT
Truncate database failed because TMPDIR is not set correctly\n
Replace database failed because TMPDIR is not set correctly\n
parameters
variable number must be between ?1 and ?%d
non-%s value in %s.%s
attempt to write a readonly database
_rowid_, *
denying fcntl on invalidated fd %d
%s prohibited in %s
sqlite_drop_constraint
HAS_CODEC_RESTRICTED
textrekey
Wrong number of columns for an rtree table
%s%.3x+%.6x
PRAGMA 
invalid change: defined value in PK of new.* record
SQLITE_ENABLE_SEE
SpringBoard
partial
AUTOINCREMENT is only allowed on an INTEGER PRIMARY KEY
%2d
Page %u: never used
sqlite_rename_table
%u-ROW VALUES CLAUSE
SELECT size FROM %Q.'%q_docsize' WHERE docid=?
munmap
spotlightknowledged.updater
%s: \"%s\" - should this be a string literal in single-quotes?
GROUP BY
ENABLE_FTS5
CREATE TABLE ['\"]*
unix-proxy
unlinked
Integer
frame ending offset must be a non-negative integer
access permission denied
fts5vocab
syslog
quick_check
(join-%u)
Integrity check failed: %s
IntCopy
FinishSeek
RESTRICT
DELETE FROM %Q.'%q_content' WHERE rowid = ?
fts5 expression tree is too large (maximum depth %d)
Param
atanh
ENABLE_PERCENTILE
UPDATE main.
CASCADE
CREATE TABLE %Q.%s(%s)
UPDATE %Q.'%q_segdir' SET idx = ? WHERE level=? AND idx=?
malformed tokendata=... directive
, 1
group_concat
PRAGMA table_list
analysis_limit
SELECT 
unix-none
N.
nsurlstoraged
NULL value in %s.%s
SeekGT
sqlite3_get_table() called with two or more incompatible queries
AUTOMATIC COVERING INDEX
ent
RELEASE fts3
docsize
case_sensitive
read error (len %d)
misuse of aggregate: %#T()
unsafe use of virtual table \"%s\"
exclusive
logi
icate
attempt to open \"%s\" as file descriptor %d
SCopy
UTF16be
name=%Q AND sql=%Q
cannot override %s of window: %s
%z%s?%d
,%.*s REAL
onoffalseyestruextrafull
DEFAULT_CACHE_SIZE=128
INSERT INTO 
Not
sz
200
unknown function: %#T()
excluded
jsonb_group_array
-
temp_store_directory
,arg HIDDEN
sqlite_version
percentile_cont
DROP TABLE IF EXISTS %Q.'%q_segments';DROP TABLE IF EXISTS %Q.'%q_segdir';DROP TABLE IF EXISTS %Q.'%q_docsize';DROP TABLE IF EXISTS %Q.'%q_stat';%s DROP TABLE IF EXISTS %Q.'%q_content';
sqllogFindFile(): error reading index file
testfixture
SQLITE_ACCEPTABLE_OVERALL_VM_STEP
IdxGE
PRAGMA main.cache_size
/tmp
real
parse error in tokenize directive
crisismerge
status
jsonb_array_insert
DROP TABLE IF EXISTS %Q.'%q_data';DROP TABLE IF EXISTS %Q.'%q_idx';DROP TABLE IF EXISTS %Q.'%q_config';
foreign key mismatch - \"%w\" referencing \"%w\"
contentless_delete=1 requires a contentless table
Found
Lt
Insert
statement too long
row not in PRIMARY KEY order for %s
sum
segments
vtable constructor called recursively: %s
Invalid key value
:memory:
too many terms in %s BY clause
\n)
edit constraints of
invalid Unicode escape
remove_diacritics=0
SELECT count(*) FROM %Q.'%q_segdir' WHERE level = ?
unix-excl
file unlinked while open: %s
SELECT*FROM\"%w\".%s ORDER BY rowid
CREATE VIRTUAL TABLE temp.%Q USING %Q
hard_heap_limit
a NATURAL join may not have an ON or USING clause
zeroblob
DELETE FROM %Q.'%q_content'
iveness
ou
ENABLE_SQLLOG
table %s may not be indexed
iss
ment
leaf
%s-shm
pipelined
count_changes
BLOOM FILTER ON %S (
INDEX %s
iif
DELETE FROM %Q.'%q_segdir' WHERE level BETWEEN ? AND ?
%_parent
%z%s\"%w\".\"%w\".\"%w\"=\"%w\".\"%w\".\"%w\"
%s_%05d.sql
SorterInsert
sqllogCopydb(): error backing up database
LZFSE
SoftNull
Extends off end of page
locking protocol
fcntl
wrong number of arguments to function %#T()
COMPOUND QUERY
SELECT CASE WHEN quick_check GLOB 'CHECK*' THEN raise(ABORT,'CHECK constraint failed') WHEN quick_check GLOB 'non-* value in*' THEN raise(ABORT,'type mismatch on DEFAULT') ELSE raise(ABORT,'NOT NULL constraint failed') END  FROM pragma_quic
cannot drop %s column: \"%s\"
jsonb_remove
fts5: %s queries are not supported (detail!=full)
alli
pragma page_size
failed to open temp database '%s' to reset truncated database %s with flags %x: %d\n
input to %%s() is not numeric
Subtract
NEAR
er
INSERT INTO\"%w\".\"%w_rowid\"(rowid,nodeno)VALUES(?1,?2)ON CONFLICT(rowid)DO UPDATE SET nodeno=excluded.nodeno
16LE
there is already a table named %s
%sON CONFLICT clause does not match any PRIMARY KEY or UNIQUE constraint
total
Freelist: 
inf
fts5_insttoken
DEFAULT_WAL_AUTOCHECKPOINT=1000
%s
/**** ERROR: (%d) %s *****/\n
ElseEq
too many columns in %s
DropIndex
pragma encoding = %s;\n
RIGHT
jsonb
AND
data
bad JSON path: %Q
cannot drop column \"%s\": no other columns exist
unhex
bl
Cannot add a PRIMARY KEY column
, l%d
 SET 
foreign key
temporary
/dev/null
invalid rootpage
secure_delete
ROLLBACK
name='%q' AND type='index'
PARTITION clause
unable to validate the inverted index for FTS5 table %s.%s: %s
VNext
INT
id INTEGER PRIMARY KEY
DELETE FROM '%q'.'%q_rowid' WHERE rowid = ?1
-1e999
SorterNext
function_list
9e999
sqlite_compileoption_get
/Notes/notes.sqlite
/dev/urandom
%d
%!0.17g
SELECT idx FROM %Q.'%q_segdir' WHERE level=? ORDER BY 1 ASC
fts5: corruption found reading blob %lld from table \"%s\"
Sort
IdxDelete
frame ending offset must be a non-negative number
ON
malformed inverted index for FTS5 table %s.%s
categories
PRAGMA main.journal_mode
DropTrigger
foreign_keys
REPLACE INTO %Q.'%q_stat' VALUES(?,?)
PRAGMA defer_foreign_keys = 0
DELETE FROM sqlite_sequence;\n
.0
flags
CREATE TABLE x(key,value,type,atom,id,parent,fullkey,path,json HIDDEN,root HIDDEN)
SELECT nodeno FROM '%q'.'%q_rowid' WHERE rowid = ?1
sqliteplocks
DropTable
%Q.%Q
unix-afp
detail
wal_checkpoint
(\"%s\"
DELETE FROM %Q.sqlite_master WHERE name=%Q AND type='index'
trigger %T already exists
wrong number of arguments to function fts5_get_locale()
seqno
multiple content=... directives
x'
(%s%u)
AggValue
random
power
pm
%.3f
alg
sqlite_find_constraint
database disk image is malformed
DESC
auto-index
json_valid
view
%c%04d-%02d-%02d %02d:%02d:%06.3f
SELECT level, idx, end_block FROM %Q.'%q_segdir' WHERE level BETWEEN ? AND ? ORDER BY level DESC, idx ASC
,%s%s%s
reverse_unordered_selects
generated
cannot INSERT into generated column \"%s\"
Program
frame starting offset must be a non-negative number
json_pretty
ence
ambiguous column name
UPDATE \"%w\".sqlite_master SET sql = sqlite_add_constraint(sqlite_drop_constraint(sql, %d), %.*Q, %d) WHERE type='table' AND tbl_name=%Q COLLATE nocase
REPLACE INTO '%q'.'%q_data'(id, block) VALUES(?,?)
In RTree %s.%s:\n%z
MAX_FUNCTION_ARG=127
sql_read_archive_header('%s') failed with errno %d
/****** %s ******/\n
*** 
k(%d
]
IncrVacuum
/*+%d bytes*/
INSERT INTO %Q.sqlite_master VALUES('index',%Q,%Q,#%d,%Q);
too many terms in compound SELECT
+- \n\t0123456789
cannot open view: %s
full_fsync
start of 
INSERT INTO %Q.%Q(%Q) VALUES('flush')
openDirectory
DecrJumpZero
CREATE TABLE 
trigram
BitAnd
cache_size
mmap_size
ieee754_mantissa
unknown database: %s
%.4c%s%.16c
tclsh
SCAN %S
aliti
Gosub
SCAN CONSTANT ROW
%s clause should come after %s not before
merge
read
suggestd
.\"%.*s\"
LIKE or GLOB pattern too complex
expr_compare
version
insttoken
NO
encoding
DISTINCT aggregates must have exactly one argument
unsupported encoding: %s
</b>
%d %d %d %d 
expected integer, got \"%.*s\"
idx IS CASE WHEN length(?4)=0 AND typeof(?4)='blob' THEN NULL ELSE ?4 END 
Column
callservicesd
timeout
degrees
localtime
failed memory resize %u to %u bytes
REPLACE INTO %Q.'%q_segdir' VALUES(?,?,?,?,?,?)
\\012
BeginSubrtn
MaxPgcnt
MobileNotes
 values differ from index 
REPLACE INTO %Q.'%q_segments'(blockid, block) VALUES(?, ?)
must specify either filename= or data= but not both
com.apple.sqlite
trigger
entitlement \"%s\" required to activate SEE
flexnum
TEXT value in %s.%s
NO ACTION
file:
\"%w\"
ROLLBACK TO fts3
destination database is in use
pragma page_size = %d;\n
memdb(%p,%lld)
row value misused
SELECT %s FROM \"%w\".\"%w\" WHERE NOT EXISTS (  SELECT 1 FROM \"%w\".\"%w\" WHERE %s)
linked
REUSE SUBQUERY %d
table %s has %d values for %d columns
DISTINCT is not supported for window functions
UPDATE temp.sqlite_master SET sql = sqlite_rename_quotefix('temp', sql)WHERE name NOT LIKE 'sqliteX_%%' ESCAPE 'X' AND sql NOT LIKE 'create virtual%%'
pragma user_version = %d;\n
\n;\n
msdos
optimize
DELETE FROM %Q.%s
failed to allocate %u bytes of memory
ALTER TABLE %Q.'%q_node'   RENAME TO \"%w_node\";ALTER TABLE %Q.'%q_parent' RENAME TO \"%w_parent\";ALTER TABLE %Q.'%q_rowid'  RENAME TO \"%w_rowid\";
json_remove
/Library/AddressBook/AddressBookImages.sqlitedb
simple
SUBSTR_COMPATIBILITY
delete
LZ4_RAW
wal_autocheckpoint
UPDATE temp.sqlite_master SET sql = sqlite_rename_column(sql, type, name, %Q, %Q, %d, %Q, %d, 1) WHERE type IN ('trigger', 'view')
column= value must be positive
Or
itunesstored
TMPDIR
SELECT tbl,idx,stat FROM %Q.sqlite_stat1
id INTEGER PRIMARY KEY, sz BLOB
cannot UPSERT a view
full
bad schema: '%s' - %s
%s;\n%s
API called with finalized prepared statement
MJ delete: %s
tokendata
dbstat
%s; -- clock=%d\n
ieee754_inc
path error (len %d)
, c%d
Auto logging environment variable set, but process is restricted. Ignoring.
AutoCommit
p2
 USING COVERING INDEX 
ism
hexrekey
DEFAULT_SECTOR_SIZE=4096
second argument to nth_value must be a positive integer
ieee754_to_int
volume does not support data protection, stripping SQLITE_OPEN_FILEPROTECTION_* flags
file-read-metadata
Blob
misuse of %s function %#T()
views may not be indexed
fts5: corruption in table \"%s\"
rename
%!S
 REAL
auto
Move
tbl
index expressions
C
pragma auto_vacuum = %s;\n
BLOB
textkey
CREATE TABLE x(value,pointer hidden,count hidden,ctype hidden)
constraint may not be dropped: %s
no such view
not an array element: %Q
too many arguments on %s() - max %d
ESCAPE expression must be a single character
SELECT level, count(*) AS cnt FROM %Q.'%q_segdir'   GROUP BY level HAVING cnt>=?  ORDER BY (level %% 1024) ASC, 2 DESC LIMIT 1
stderr
%
UPDATE %Q.sqlite_master SET type='table', name=%Q, tbl_name=%Q, rootpage=0, sql=%Q WHERE rowid=#%d
trunc
missing %s parameter in fts4 constructor
segdir
CREATE TABLE %Q.'%q_%q'(%s)%s
non-integer argument passed to function fts5_get_locale()
SYSTEM_MALLOC
Once
IfNotOpen
%02d
Index already optimal
no such fts5 table: %s.%s
<dst path null>
subtype
HaltIfNull
%s.%z
argument of ntile must be a positive integer
at
Node %lld is too small (%d bytes)
ENABLE_CARRAY
ROLLBACK TO changeset_apply
VACUUM \"%w\" INTO '%q'
Dimension %d of cell %d on node %lld is corrupt
circular reference: %s
biomesyncd
BitOr
empty_result_callbacks
open flag(s) 0x%08x are reserved for VFS use and do not affect behaviour when passed to sqlite3_open_v2
rowid
Pagecount
 UNIQUE
failed to get page %u
unsupported frame specification
cos
time
%s: table does not support scanning
cannot open table with generated columns: %s
unlink
vtable constructor failed: %s
coll
UTF-16le
array_insert
ble
phrase
ALTER TABLE %Q.'%q_segdir'   RENAME TO '%q_segdir';
FLAGS parameter to json_valid() must be between 1 and 15
 WITHOUT ROWID
SQLite ARCHIVE_APPLE_1
INSERT INTO sqlite_schema(type,name,tbl_name,rootpage,sql)VALUES('table','%q','%q',0,'%q');
@  
too many attached databases - max %d
invalid arguments to fts4aux constructor
sqllogFindFile(): error in fopen()
SQLite format 3
v8@?0
%s %S%s
replace
row
dummy
Expire
ANALYZE \"%w\".\"%w\"
CREATE TABLE \"%w\".\"%w_rowid\"(rowid INTEGER PRIMARY KEY,nodeno
rekey
ceil
, x.%Q
tmpsqlitearchiveXXXXXX
CollSeq
ATTACH %Q AS %s
automatic_index
hexkey
virtual tables may not be indexed
tan
while executing statement ('%s') it failed with error code %d and reason:'%s'\n
exfat
\\u00
fts3_tokenizer requires bound parameters
compression_stream_init failed for %d\n
thstndrd
ORDER BY without LIMIT on %s
implies_nonnull_row
compression_stream_process
SELECT name, type, sql FROM \"%w\".sqlite_schema WHERE sql NOT NULL AND type=='table' AND name!='sqlite_sequence'
BEGIN IMMEDIATE; COMMIT;
internal query planner error
frame specification
%s unfinalized statement
id INTEGER PRIMARY KEY, sz BLOB, origin INTEGER
DEFAULT_AUTOVACUUM
id
round
the fraction argument to %%s() is not the same for all input rows
,\n  
legacy_alter_table
generated column loop on \"%s\"
no such column
database schema has changed
must have at least one non-generated column
SELECT %s FROM %s T WHERE T.%Q=?
INSERT INTO '%q'.'%q_idx'(segid,term,pgno) VALUES(?,?,?)
ENABLE_SESSION
SELECT sql FROM \"%w\".sqlite_schema WHERE sql NOT NULL  AND type IN ('index','trigger','view')  AND tbl_name=%Q COLLATE nocase
temporary storage cannot be changed from within a transaction
a CHECK constraint
20e
CREATE TABLE IF NOT EXISTS %Q.'%q_stat'(id INTEGER PRIMARY KEY, value BLOB);
MAX_PAGE_COUNT=1073741823
PRAGMA journal_mode=WAL
columns
rtreenode
indexed
at most %d tables in a join
SeekScan
rtrim
%z%s%z
Yield
partial index WHERE clauses
%r ORDER BY term does not match any column in the result set
non-unique entry in index 
MAX_VARIABLE_NUMBER=500000
no such column: \"%s\"
IsType
hidden
jsonb_each
%s_segments
highlight
Node %lld missing from database
stmt-pointer
freeonclose
RowSetRead
RECURSIVE STEP
normal
error in %s %s%s%s: %s
%.*s%s
rtreedepth
MUTEX_UNFAIR
immutable
trusted_schema
like
no such index: %S
a generated column
bytecode
INTERSECT
a JOIN clause is required before %s
program
failed to set lock proxy file
 AND (?6 OR ?3 IS stat)
ATTACH
FkCounter
index_info
-- TRIGGER %s
temporary trigger may not have qualified name
json_extract
more than one 'header' parameter
unrecognized matchinfo: %s
query aborted
cannot change %s wal mode from within a transaction
0123456789ABCDEF0123456789abcdef
fstat
%s(%d)
Permutation
CREATE TABLE %Q.sqlite_sequence(name,seq)
multiple references to recursive table: %s
BEGIN
modeof
QNaN
50f-20a-20d
fts5
node
DQS=3
sqlite_sequence
PRAGMA cache_size=%d
user_version
corrupt schema
r
SELECT sql FROM \"%w\".sqlite_schema WHERE type='table'AND name<>'sqlite_sequence' AND coalesce(rootpage,1)>0
hybridsearchd
UPDATE %Q.sqlite_master SET rootpage=%d WHERE #%d AND rootpage=#%d
vfs
Node %lld is too small for cell count of %d (%d bytes)
no such function: %#T
SETUP
DEFAULT_FILE_FORMAT=4
If
\n  
%z%s%Q
.\"
JournalMode
DeferredSeek
column%d
UPDATE OR FAIL %Q.'%q_segdir' SET level=-1,idx=? WHERE level=? AND idx=?
recursively defined fts5 content table
WHERE name=%Q
unable to delete/modify collation sequence due to active statements
IdxRowid
searchd
index_xinfo
second argument to %#T() must be a constant between 0.0 and 1.0
Cannot add a column to a view
error parsing prefix parameter: %s
unable to validate the inverted index for FTS%d table %s.%s: %s
SELECT sz%s FROM %Q.'%q_docsize' WHERE id=?
Prev
non-deterministic functions
close deferred due to
Copy
Child page depth differs
page_count
type
automatic index on %s(%s)
%.*s %s%s
%s_data
sqlite3changeset_apply(): primary key mismatch for table %s
pragma journal_mode=wal
Delete
/Calendar/Calendar.sqlitedb
\t Attempted temporary directory at path '%s' with stat() errno %d and access errno %d%s\n
INDEX %d
triggers nested too deep
vacuum_%016llx
jsonb_tree
LEFT
Safety level may not be changed inside a transaction
unknown special query: %.*s
SELECT parentnode FROM '%q'.'%q_parent' WHERE nodeno = ?1
header
unsupported use of NULLS %s
not an error
PRAGMA user_version
BUG IN CLIENT OF libsqlite3.dylib: database integrity compromised by API violation: vnode %s while in use: %s
p4
,%s(x.'c%d%q')
SELECT pgno FROM '%q'.'%q_idx' WHERE segid=? AND term<=? ORDER BY term DESC LIMIT 1
 %g
UTF-8
com.apple.libsqlite3
sqlite_temp_master
DELETE FROM %Q.'%q_docsize';
-- Main database is '%q'\n
rowid=?
noop
the fraction argument to %%s() is not between 0.0 and %.1f
INSERT OR REPLACE INTO '%q'.'%q_parent' VALUES(?1, ?2)
'%.*q'
 WHERE <expr>
UPDATE \"%w\".sqlite_master SET sql = sqlite_drop_constraint(sql, %s) WHERE type='table' AND tbl_name=%Q COLLATE nocase
DELETE FROM %Q.'%q_content' WHERE id=?
table_list
notindexed
pragma legacy_file_format
ftruncate
ZeroOrNull
AggFinal
double
index associated with UNIQUE or PRIMARY KEY constraint cannot be dropped
source and destination must be distinct
SELECT * FROM %Q.sqlite_schema
apfs
mmap
cell_size_check
no such collation sequence: %s
sqlite_detach
asin
SQLite 
Cast
%s: %s.%s
%s unfinished backup
malformed inverted index for FTS%d table %s.%s
bm25
_node
acos
SELECT count(*) FROM %Q.'%q_%s'
 WHERE rowid=?1
DROP INDEX IF EXISTS \"%w\"
vtable constructor did not declare schema: %s
%s mode not allowed: %s
too many prefix indexes (max %d)
compression_stream_destroy
end
<unresolvable path>
unixReplaceDatabase() failed with error %d for replacing '%s' with '%s' \n
%d values for %d columns
getcwd
..%s
Sqlite_Heap_homed
rtreecheck
ENABLE_API_ARMOR
duplicate column name: %s
multiple content_rowid=... directives
fchown
SQLITE_EXEMPT_PATH_FROM_VNODE_GUARDS
old
: 
aes256
NaN
-- %s
sissii
PRAGMA %Q.data_version
no such cursor: %lld
pragma application_id = %d;\n
select name,sql from sqlite_master where type = 'index' and rootpage != 0
config
IfNot
misuse of aliased aggregate %s
CREATE%s INDEX %.*s
database %s is locked
UPDATE \"%w\".sqlite_master SET sql = sqlite_rename_column(sql, type, name, %Q, %Q, %d, %Q, %d, %d) WHERE name NOT LIKE 'sqliteX_%%' ESCAPE 'X'  AND (type != 'index' OR tbl_name = %Q)
Schema corrupt or not an rtree
,a%d
uuid_blob
ShiftRight
SorterOpen
CHECK
Tree %u page %u: 
strftime
jsonb_insert
database or disk is full
%z, langid
sql dump
FkCheck
%z: %s
%04d
logging-persist
ShiftLeft
infinity
object name reserved for internal use: %s
stat_push
SELECT coalesce((SELECT max(blockid) FROM %Q.'%q_segments') + 1, 1)
open('%s') failed with errno %d
 is never used
AggStep
file
tional
entli
string or blob too big
malformed database schema (%s)
ational
CODEC=see-cccrypt
Clear
bird
synchronous
row 
MAX_ATTACHED=10
DELETE FROM main.
cannot start a transaction within a transaction
recursive reference in a subquery: %s
parameters are not allowed in views
CREATE TABLE %Q.'%q_segdir'(level INTEGER,idx INTEGER,start_block INTEGER,leaves_end_block INTEGER,end_block INTEGER,root BLOB,PRIMARY KEY(level, idx));
ASC
<
integer
%s: %s.%s.%s
NONE
MobileSafari
ncol
after drop column
table schemas do not match
SequenceTest
Offset %u out of range %u..%u
file is not a database
unrecognized column option: %s
PRAGMA writable_schema=OFF;\n
tmpsqlitetruncatedbXXXXXX
integrity_check
utc
unpinned
RELEASE changeset_apply
cannot open %s column for writing
misuse of aliased window function %s
SQLITE_ENABLE_VNODE_GUARDS
user 'setup'(248) opening database '%s' with SQLITE_OPEN_READWRITE
CREATE TABLE x(
syntax error
SELECT 1 FROM sqlite_master LIMIT 1
grindrx
MakeRecord
SET DEFAULT
--
GooglePhotos
strict
stat_get
MAX_COMPOUND_SELECT=500
-wal
always
custom
%.16g
error in generated column \"%s\"
duplicate WITH table name: %s
concat_ws
ContactsCoreSpotlightExtension
unknown tokenizer
CREATE TABlE vocab(term, doc, col, offset)
argument to %s() is not a valid SQL statement
null
readlink
SeekGE
overflow list length
irb
coalesce
INSERT INTO %Q.'%q_content' VALUES(%s)
MAX_WORKER_THREADS=8
ResetCount
 (
c
NUMERIC value in %s.%s
local time unavailable
rb
,
USING INDEX %s FOR IN-OPERATOR
jsonb_array
Ne
jsonb_patch
}
%Q.
rmdir
zeroblob(%d)
notnull
expressions
40f
CREATE TABLE x(addr INT,opcode TEXT,p1 INT,p2 INT,p3 INT,p4 TEXT,p5 INT,comment TEXT,subprog TEXT,nexec INT,ncycle INT,stmt HIDDEN);
DEFAULT_RECURSIVE_TRIGGERS
there is already an index named %s
SCAN %d CONSTANT ROW%s
 FROM '%q'.'%q%s' AS x
ENABLE_MATH_FUNCTIONS
ENABLE_SNAPSHOT
%z%s\"%w\".\"%w\".\"%w\"
 AND (?%d OR ?%d IS %w.%w)
denying truncate of invalidated fd %d
PRAGMA cache_spill=%d
incomplete input
 of index 
DELETE FROM %Q.'%q_segdir'
eed
Int64
statement aborts at %d: %s; [%s%s]
threads
not authorized to use function: %#T
 NUM
%d:%s
cannot fstat db file %s
siriknowledged
/*scan*/
rowid not at end-of-record for row 
json_group_array
Too few columns for an rtree table
%s%.3x/
ENABLE_FTS4
builtin
too many terms in ORDER BY clause
 LEFT-JOIN
matchinfo
Dimension %d of cell %d on node %lld is corrupt relative to parent
Remainder
RANGE with offset PRECEDING/FOLLOWING requires one ORDER BY expression
use DROP VIEW to delete view %s
u
shared
SELECT rowid, rank FROM %Q.%Q ORDER BY %s(\"%w\"%s%s) %s
sqlite3
medialibraryd
compression_stream_process failed for %d\n
;\n
schema
access to view \"%s\" prohibited
typeof
languageid
lock_proxy_file
fkid
utf16le
am
undefined
PRAGMA main.cache_spill
IfPos
OpenAutoindex
journal_mode
 
unable to close due to unfinalized statements or unfinished backups
DEFAULT_MMAP_SIZE=0
/
logging
too many FROM clause terms, max: %d
incremental
segid, term, pgno, PRIMARY KEY(segid, term)
PRAGMA '%q'.table_xinfo('%q')
unix-flock
open
truncated
And
USE TEMP B-TREE FOR %sORDER BY
MATCH
reserved fts5 table name: %s
alism
cannot open file
DISTINCT
flags must include SQLITE_OPEN_READONLY or SQLITE_OPEN_READWRITE
DELETE FROM '%q'.'%q_idx' WHERE (segid, (pgno/2)) = (?1, ?2)
CREATE TABLE x(value INTEGER PRIMARY KEY)
Rowid %lld out of order
unrecognized token: \"%T\"
index %s already exists
atan
%z, 'c%d%q'
ENABLE_FTS3_TOKENIZER
activate_extensions
order
remove_diacritics
DROP TABLE IF EXISTS %Q.'%q_docsize';
VACUUM
%s/etilqs_%llx%c
SELECT idx, start_block, leaves_end_block, end_block, root FROM %Q.'%q_segdir' WHERE level = ? ORDER BY idx ASC
tables_used
Next
Sqlite_Heap
wrong number of arguments to function highlight()
IdxLE
an index
unknown operation
parse error in \"%s\"
cannot VACUUM from within a transaction
_ROWID_
UTF-16
%.*s%s%s
Too many entries in SQLITE_EXEMPT_PATH_FROM_VNODE_GUARDS, truncating list to first %d entries
 INT
content
ORDER
recursive aggregate queries not supported
changes
MAX_EXPR_DEPTH=1000
OMIT_LOAD_EXTENSION
/* %s */ 
page_size
%sSCALAR SUBQUERY %d
MATERIALIZE %!S
now
%s %T already exists
*]
, 
disk I/O error
Mapping (%lld -> %lld) missing from %s table
YES
RowSetTest
incremental_vacuum
temporary table name must be unqualified
IdxLT
unsupported file format
ignore_check_constraints
the NOT INDEXED clause is not allowed on UPDATE or DELETE statements within triggers
homed
ascii
 FROM 
CREATE TABLE %Q.'%q_docsize'(docid INTEGER PRIMARY KEY, size BLOB);
, T.l%d
Invalid argument to rtreedepth()
Transaction
al
VIEW
default value of column [%s] is not constant
drop column from
SELECT max(level) FROM %Q.'%q_segdir' WHERE level BETWEEN ? AND ?
able
undersize RTree blobs in \"%q_node\"
PRAGMA page_count
CREATE TABLE x(type text,name text,tbl_name text,rootpage int,sql text)
printf
ceiling
fulness
Source file '%s' is not an SQLite database file, or is encrypted.  Type is %d
com.apple.private.sqlite.sqlite-encryption
Replacement SPI only supports encrypted databases when keys match
16BE
VOpen
p5
rows inserted
integrity-check
BEGIN DEFERRED; PRAGMA schema_version
vtab:%p
flgs
rows deleted
sqlite_drop_column
json_object() labels must be TEXT
rebuild
%s_%s.db
compression_stream_init
PRAGMA table_info=%Q
ieee754_from_blob
nfs
GetSubtype
%03d
FTS expression tree is too large (maximum depth %d)
ENABLE_DBSTAT_VTAB
stat
SeekEnd
too many arguments on function %T
Cannot add a UNIQUE column
subsec
UNIQUE
ValueList
ative
DEFAULT_PCACHE_INITSZ=20
:auto:
MustBeInt
keybagd
sqlite_stat4
fts5: checksum mismatch for table \"%s\"
Failed to confine fd %d for file %s (%d): %s
%s %T cannot reference objects in database %s
UPDATE \"%w\".sqlite_master SET sql = sqlite_rename_quotefix(%Q, sql)WHERE name NOT LIKE 'sqliteX_%%' ESCAPE 'X' AND sql NOT LIKE 'create virtual%%'
unlikely
%04d-%02d-%02d
DROP TABLE IF EXISTS %Q.'%q_content';
freelist leaf count too big on page %u
multiple recursive references: %s
%s unfinalized statement: \"%s\"
notification message
ioctl
IntelligencePlatformComputeService
OpenDup
UPSERT not implemented for virtual table \"%s\"
%.*s, %s%s
%Q
SELECT (SELECT max(idx) FROM %Q.'%q_segdir' WHERE level = ?) + 1
argument type mismatch
on_update
virtual tables may not be altered
SQLITE_SQLLOG_DIR
RealAffinity
Compare
cannot open value of type %s
Cannot add a NOT NULL column with default value NULL
DELETE FROM %Q.'%q_segments'
SeekHit
unable to open database: %s
, x.'%q'
SELECT parentnode FROM %Q.'%q_parent' WHERE nodeno=?1
SELECT name, type, sql FROM \"%w\".sqlite_schema WHERE name=='sqlite_sequence'
unixWrite
bind on a busy prepared statement: [%s]
LEFT-MOST SUBQUERY
 AND 
UPDATE \"%w\".sqlite_master SET sql = printf('%%.%ds, ',sql) || %Q || substr(sql,1+length(printf('%%.%ds',sql))) WHERE type = 'table' AND name = %Q
AddImm
octet_length
attached databases must use the same text encoding as main database
column index out of range
prefix
iz
ible
ENABLE_BYTECODE_VTAB
(blob)
name
default
 ORDER BY name
no
\\n
tmpsqlitereplacedbXXXXXX
too many columns on %s
unknown datatype for %s.%s: \"%s\"
SELECT data FROM %Q.'%q_node' WHERE nodeno=?
tbl, ?2, stat
last write ended with return %ld expected %ld with errno %d\n
cannot store %s value in %s column %s.%s
unable to get the page. error code=%d
\\u0000
fts5: missing row %lld from content table %s
MAX_DEFAULT_PAGE_SIZE=8192
COMMIT;\n
%s.%s.%s
DELETE FROM %Q.sqlite_master WHERE tbl_name=%Q and type!='trigger'
fts5_locale
recursive definition for %s.%s
ENABLE_LOCKING_STYLE=1
bad parameter: '%s'
statfs
shrink_memory
shadow
json_insert
RowCell
SELECT length(data) FROM '%q'.'%q_node' WHERE nodeno = 1
multiple links to file: %s
%sLIST SUBQUERY %d
%!.*f
compress
docid
SELECT %s%s FROM %Q.%Q WHERE (%s) IS (%s)
Trace
atan2
pi
SELECT * FROM (SELECT 'sqlite_schema' AS name,1 AS rootpage,'table' AS type UNION ALL SELECT name,rootpage,type FROM \"%w\".sqlite_schema WHERE rootpage!=0)
authorization denied
write
affected by unexpected operation
database table is locked: %s
collation_list
cannot join using column %s - column not present in both tables
sqlite_returning_%p
jsonb_extract
invalid fts5 file format (found %d, expected %d or %d) - run 'rebuild'
VCheck
index corruption
database
issisii
Cannot add a REFERENCES column with non-NULL default value
rename columns of
unable to close due to
ed
unix
subrtnsig:%d,%s
sqlite_fail
ENABLE_COLUMN_METADATA
origin
total_changes
set
no such table: %s
%s references tables to its right
cannot UPDATE generated column \"%s\"
malformed contentless_delete=... directive
%s a subset of columns on fts5 contentless-delete table: %s
ALTER TABLE %Q.'%q_%s' RENAME TO '%q_%s';
PRAGMA database_list
%z - %s
AM
col
DIRECT_OVERFLOW_READ
queries
healthd
Overriding cache_size %d -> %d
unindexed
DEFAULT_JOURNAL_SIZE_LIMIT=32768
ERROR: sqlite database is locked because it is in use by another host that holds a host-exclusive lock on %s; this host (UUID %s) cannot override the host-exclusive lock until the other host (UUID %s) releases its locks on %s\n
utf16be
invalid uri authority: %.*s
view %s may not be altered
unable to use function %s in the requested context
\\015
IsTrue
AUTOINCREMENT not allowed on WITHOUT ROWID tables
datatype mismatch
unable to delete/modify user-function due to active statements
overflow
CreateBtree
invalid
fts5_get_locale
pragma application_id
match
virtual
expected %d columns for '%s' but got %d
REPLACE INTO %Q.'%q_docsize' VALUES(?,?)
malformed prefix=... directive
'delete-all' may only be used with a contentless or external content fts5 table
0123456789abcdef
INTEGER
temp
IfSizeBetween
tanh
malformed locale=... directive
SET NULL
CREATE VIRTUAL TABLE %T
REPLACE INTO %Q.'%q_config' VALUES(?,?)
BUG_COMPATIBLE_20160819
sqlite_
'%s'
no such table
database is already attached
percentile
Eq
pgsz
DELETE FROM %Q.'%q_content';
API call with %s database connection pointer
COVERING INDEX %s
Inf input to %%s()
SAVEPOINT replace_op
denying shm read from invalidated fd %d
cache_spill
desc
unknown table option: %.*s
database %s is already in use
hex
no such constraint: %s
CREATE TABLE \"%w\".\"%w_parent\"(nodeno INTEGER PRIMARY KEY,parentnode);
CursorUnlock
pragma journal_mode = wal
julianday
INSERT INTO \"%w\".\"%w_node\"VALUES(1,zeroblob(%d))
DROP TABLE '%q'.'%q_node';DROP TABLE '%q'.'%q_rowid';DROP TABLE '%q'.'%q_parent';
pread
failed to set '%s' on truncated database %s, %d: %s\n
new
DELETE FROM %Q.sqlite_sequence WHERE name=%Q
%s.xBestIndex malfunction
cannot use RETURNING in a trigger
near \"%T\": syntax error
->>
json_object
offsets
?%d
MobileMail
os_unix.c:%d: (%d) %s(%s) - %s
LoadAnalysis
DELETE FROM %Q.%s WHERE %s=%Q
com.apple.private.sqlite.defensive
rename failed (%d)
/var/tmp
Last
integer overflow
, NULL
DELETE FROM '%q'.'%q_node' WHERE nodeno = ?1
ENABLE_NORMALIZE
invalid change: column %d is undefined
entitlement \"%s\" or environment variable \"SQLITE_ENABLE_SEE=1\" required to activate SEE
there is already another table or index with this name: %s
USE TEMP B-TREE FOR %s(ORDER BY)
-journal
table
\\\"
pragma_
aggregate
too many SQL variables
pow
FOREIGN KEY constraint failed
_rowid_
routined
SELECT * FROM %Q.%Q
CREATE TABLE %Q.'%q_content'(%s)
oid
TraceSQL(%p): %s\n
fallocate
%s in \"%s\"
sqlite_autoindex_%s_%d
format
mod
json_group_object
file renamed while open: %s
memdb
set list
SELECT k, v FROM %Q.'%q_config'
bli
PRAGMA foreign_keys=OFF;\nBEGIN TRANSACTION;\n
>
sqlite_rename_test
\"%w\" 
ENABLE_PREUPDATE_HOOK
1e999
abbreviated query algorithm search
ORDER BY without LIMIT on UPDATE
SELECT %s WHERE rowid = ?
ReleaseReg
CREATE TABlE vocab(term, col, doc, cnt)
carray-bind
/iTunes/MediaLibrary.sqlitedb
orphan index
year
pragma user_version
json_quote
unknown error
Index optimized
%Q%s
bad parameter or other API misuse
remove_diacritics=1
%Q, 
INSERT INTO main.
SorterCompare
index '%q'
fts3_tokenizer
DELETE FROM %Q.'%q_docsize'
SELECT value FROM %Q.'%q_stat' WHERE id=?
database corruption
DEFAULT_CKPTFULLFSYNC
CREATE VIRTUAL TABLE
=%Q
sqrt
20c:20e
%06.3f
merge=
alize
);CREATE TABLE \"%w\".\"%w_node\"(nodeno INTEGER PRIMARY KEY,data);
MAX_MMAP_SIZE=20971520
RTRIM
block
ate
%s,%u,%u,0x%llx,0x%llx,0x%llx,%lu,0x%llx,%s\n
Explain
sqlite_add_constraint
vnguard
,schema HIDDEN
OID
target object/alias may not appear in FROM clause: %s
misuse of aggregate: %s()
,\n
separators
enci
Auxiliary rtree columns must be last
explain
index
a
%z%Q, 
%lld %lld
SQLITE_AUTO_TRACE
%z%s\"%w\".\"%w\".\"%w\" IS NOT \"%w\".\"%w\".\"%w\"
none
%.*s
IMDPersistenceAgent
no such module: %s
rows updated
SQLITE_MALLOC_ZONE
wrong number of arguments to function snippet()
reserve
exp
B
\n
case_sensitive_like
recursive_triggers
enc
json_replace
cannot open savepoint - SQL statements in progress
,%.*s
cannot open virtual table: %s
cannot rollback - no transaction is active
no tables specified
<b>
10000.0
the INDEXED BY clause is not allowed on UPDATE or DELETE statements within triggers
STMTJRNL_SPILL=131072
Variable
ORDER BY
after rename
ATOMIC_INTRINSICS=1
xctest
0x
table %s may not be modified
CREATE 
%s/sqllog_%05d
-shm
Failed to determine code signing flags
UPDATE \"%w\".sqlite_master SET sql = sqlite_rename_table(%Q, type, name, sql, %Q, %Q, %d) WHERE (type!='index' OR tbl_name=%Q COLLATE nocase)AND   name NOT LIKE 'sqliteX_%%' ESCAPE 'X'
NULL
break
persist
max_page_count
50f
RELEASE replace_op
max
ATTACH x AS %Q
Savepoint
/* unknown trigger */ 
 WHERE 
sandbox_check
sub-select returns %d columns - expected %d
CO-ROUTINE %!S
private
tbl,idx,stat
database is locked
getpagesize
sqlite_master
json_each
subqueries
type='trigger' AND name='%q'
 %llu
, T.%Q
into
localhost
trim
SELECT 2 * total(1 + leaves_end_block - start_block)   FROM (SELECT * FROM %Q.'%q_segdir'         WHERE level = ? ORDER BY idx ASC LIMIT ?  )
regexp
PRIMARY KEY
UTF-16be
%s is not supported for this process
denying read from invalidated fd %d
SQLITE_ACCEPTABLE_PAGES_PER_STEP
NewRowid
sqlite_stat?
ok
dataaccessd
wr
rwc
/Library/AddressBook/AddressBook.sqlitedb
OR
CCCRYPT256
/PhotoData/Photos.sqlite
RowData
%02x
defer_foreign_keys
tne
malformed MATCH expression: [%s]
no such tokenizer: %s
TypeCheck
inity
BBB
SELECT sql FROM sqlite_schema WHERE sql NOT NULL AND type IN ('index','trigger','view')
opcode
locking_mode
table %s may not be dropped
UPDATE %Q.'%q_segdir' SET start_block = ?, root = ?WHERE level = ? AND idx = ?
out of memory
%.*z:%u
iisX
day
Found (%lld -> %lld) in %s table, expected (%lld -> %lld)
SELECT 0, 'tbl',  '', 0, '', 1, 0     UNION ALL SELECT 1, 'idx',  '', 0, '', 2, 0     UNION ALL SELECT 2, 'stat', '', 0, '', 0, 0
pragma journal_mode = %s;\n
ion
SELECT count(*) FROM %Q.'%q%s'
radians
notused
FavoritesTodayWidget
unknown join type: %T%s%T%s%T
UPDATE %Q.sqlite_master SET tbl_name = %Q, name = CASE WHEN type='table' THEN %Q WHEN name LIKE 'sqliteX_autoindex%%' ESCAPE 'X'      AND type='index' THEN 'sqlite_autoindex_' || %Q || substr(name,%d+18) ELSE name END WHERE tbl_name=%Q COLL
SELECT %s
(subquery-%u)
BUG IN CLIENT OF libsqlite3.dylib: database integrity compromised by API violation: vnode %s while in use
Count
ization
 AND (?
sqlite3_open_v2 open failed with %d
compression_stream_process bravo failed for %d\n
i16@?0^{sqlite3_stmt=}8
SEARCH
SELECT*FROM\"%w\"
VDestroy
%_rowid
copyfile returned unsuccessfully without setting errno, assuming target path was inaccessible
API called with NULL prepared statement
no such column: \"%T\"
avg
fts4
Noop
hfs
 is not a directory
Rowid
sqllogTraceDb(): database name too long (%d bytes)
SELECTs to the left and right of %s do not have the same number of result columns
abort due to ROLLBACK
ieee754(%lld,%d)
unix-nfs
Failed to open '%s' for read/write access (%s). Attemping to open as read-only
tbl_name='%q' AND type!='trigger'
'%s' is not a function
FIRST
<src path null>
journal_size_limit
seq
SELECT name, type, sql FROM \"%w\".sqlite_schema WHERE tbl_name=%Q COLLATE nocase AND type=='table'  AND sql NOT NULL
NotExists
%s at line %d of [%.10s]
USING ROWID SEARCH ON TABLE %s FOR IN-OPERATOR
table \"%s\" has more than one primary key
delete-all
DEFAULT_MEMSTATUS=0
fcntl(%d) failed: errno=%d\n
unixShmMap-write
sqlite_compileoption_used
);
CREATE AUTOMATIC INDEX ON %s(
sssiii
ance
ator
COMPILER=clang-21.0.0
PRAGMA synchronous = 0
fts5_api_ptr
a%d=?%d
csv
%c\"%s\"
UPDATE %Q.sqlite_master SET type='%s', name=%Q, tbl_name=%Q, rootpage=#%d, sql=%Q WHERE rowid=#%d
cannot use DEFAULT on a generated column
,'%s',char(10))
ruby
sqlite_rename_quotefix
tokenchars=
REPLACE INTO %Q.'%q_config' VALUES ('version', %d)
biliti
EXCEPT
percentile_disc
CREATE TABLE %Q.'%q_segments'(blockid INTEGER PRIMARY KEY, block BLOB);
0x%x:%s
more than %d aggregate terms
MAX_SQL_LENGTH=1000000000
last read ended with return %ld with errno %d\n
replace(
smbfs
access
, T.c%d
SELECT 1 FROM pragma_index_list(%Q) WHERE origin='pk'
renamed
>? AND %s
-%T
ALTER TABLE %Q.'%q_stat'  RENAME TO '%q_stat';
read_uncommitted
window
view %s is circularly defined
 NULL
Init
assetsd
/usr/lib/libcompression.dylib
pragma journal_mode
invalid change: %s value in PK of old.* record
VInitIn
ANY
resentsd
sqlite_stat1
ReopenIdx
json_array
    
fts5: error creating shadow table %q_%s: %s
%d %s\n
.
com.apple.libsqlite3.telemetry
NoConflict
cannot create INSTEAD OF trigger on table: %S
cannot detach database %s
current_date
deletemerge
PRAGMA journal_mode=DELETE
8
true
unknown tokenizer: %s
PRAGMA writable_schema=ON;\n
recon
on_delete
UPDATE \"%w\".sqlite_sequence set name = %Q WHERE name = %Q
hw.ncpu
multiple tokenize=... directives
ANALYZE sqlite_schema;\n
biomed
freelist_count
 missing from index 
asinh
cannot UPDATE
ENABLE_STMT_SCANSTATUS
LZ4
SELECT sql FROM \"%w\".sqlite_schema WHERE type='index'
Expression tree is too large (maximum depth %d)
{}
%.18s-%s
log
trigger \"%s\" may not write to shadow table \"%s\"
mode
SELECT 1 FROM temp.sqlite_master WHERE name NOT LIKE 'sqliteX_%%' ESCAPE 'X' AND sql NOT LIKE 'create virtual%%' AND sqlite_rename_test(%Q, sql, type, name, 1, %Q, %d)=NULL 
SQL logic error
ALTER TABLE %Q.'%q_content'  RENAME TO '%q_content';
fts5: parser stack overflow
SetCookie
2nd reference to page %u
json_tree
iissssss
likely
%s.idx
BEGIN EXCLUSIVE
AlipayWallet
afpfs
InitCoroutine
no such vfs: %s
%s_stat
SQLITE_AUTO_PROFILE
DEFAULT_SYNCHRONOUS=2
LZMA
false
sqlite3changeset_apply(): no such table: %s
queries_performance
invalidated open fd: %d (0x%02lx)
%s. See syslog for more information
json_type
REPLACE INTO %Q.'%q_docsize' VALUES(?,?%s)
fts5: corrupt structure record for table \"%s\"
VBegin
INSERT INTO %Q.sqlite_master VALUES('trigger',%Q,%Q,0,'CREATE TRIGGER %q')
%02d:%02d:%02d
fts5: corruption on page %d, segment %d, table \"%s\"
mem(%p,%lld)
\\r
unix-dotfile
json_set
contentless_delete=1 is incompatible with columnsize=0
CursorLock
default_cache_size
sqllogOpenlog(): Failed to open log file
Source file '%s' is not an SQLite database file or backup archive, or is encrypted.  Type is %d
cid
blob
VIEWs and/or subqueries nested too deep
memvfs
Multiple uses for byte %u of page %u
truncate
full_column_names
sqlite\\_%
[]
pinned
unrecognized matchinfo request: %c
nolock
utf8
fts4aux
HAVE_ISNAN
create failed (%d)
Tree %u page %u right child: 
foreign_key_list
soft_heap_limit
IN(...) element has %d term%s - expected %d
array
tokenize
invalid database name \"%s\"
denying sync of invalidated fd %d
INSERT INTO %s.sqlite_schema SELECT*FROM \"%w\".sqlite_schema WHERE type IN('view','trigger') OR(type='table'AND rootpage=0)
to
struct iovec
acosh
izer
PRAGMA journal_mode=wal
seekAndRead
sqlite_stat%d
sqlite_source_id
PRAGMA defer_foreign_keys = 1
RC_XBS
ufs
Failed to read ptrmap key=%u
%r %s BY term out of range - should be between 1 and %d
pragma legacy_file_format = %d;\n
statement aborts at 
%c%u
FilterAdd
CursorHint
isisi
cannot commit - no transaction is active
pk
affinity
CREATE TABLE x(input, token, start, end, position)
no such table: %s.%s
invalid change: column %d - old.* value is %sdefined but new.* is %sdefined
invalid change: null value in PK
access to %z is prohibited
virtual table
fts3cursor
%s\"%w\" TEXT
cannot limit WAL size: %s
\"\\/bfnrt
ambiguous reference to %s in USING()
no query solution
likelihood
wal
Jump
SetSubtype
char
sin
ENABLE_RTREE
stat failed for %d\n
ClrSubtype
%s)%s
datetime
,%s(?)
INSERT INTO main.sqlite_stat1 VALUES(?1, CASE WHEN length(?2)=0 AND typeof(?2)='blob' THEN NULL ELSE ?2 END, ?3)
IfNotZero
no such savepoint: %s
noskipscan*
\"
VColumn
Fragmentation of %u bytes reported as %u on page %u
'delete' may not be used with a contentless_delete=1 table
Recursion limit
USE TEMP B-TREE FOR %s(DISTINCT)
table %s may not be altered
subsecond
rtree_i32
uuid_str
cannot add a STORED column
ZLIB
-Inf
CREATE TABLE x
sqlite_rename_column
no more rows available
duetexpert
busy_timeout
corrupt database
);\n
OMIT_AUTORESET
NOT NULL
database_list
sign
REPLACE INTO %Q.'%q_content' VALUES(%s)
wdth
FILTER clause may only be used with aggregate window functions
uncompress
END;\n
VCreate
cannot release savepoint - SQL statements in progress
frame starting offset must be a non-negative integer
month
ous
connections
table %S has no column named %s
,%.*s INT
EndCoroutine
, ?
INSERT OR REPLACE INTO '%q'.'%q_node' VALUES(?1, ?2)
MAX_VDBE_OP=250000000
VACUUM %s
Halt
s
_content
SELECT
COMMIT
checkpoint_fullfsync
generated columns cannot be part of the PRIMARY KEY
UTF16
if
RIGHT-JOIN %s
?,?,?
ALTER TABLE %Q.'%q_segments' RENAME TO '%q_segments';
pread64
Failed to set vnode guard on %s (%d): %s
corespeechd
cloudd
cannot create a TEMP index on non-TEMP table \"%s\"
%s=?
isiX
flush
instance
line %d: unescaped %c character
Ge
schema_version
SELECT sqlite_fail('constraint failed', %d) FROM %Q.%Q AS x WHERE x.%.*s IS NULL
(FK)
recovered %d pages from %s
SorterSort
OffsetLimit
conflicting ON CONFLICT clauses specified
LAST TERM OF 
SELECT sqlite_fail('constraint failed', %d) FROM %Q.%Q WHERE (%.*s) IS NOT TRUE
length
sqlite_log
SELECT NOT EXISTS(SELECT docid FROM %Q.'%q_content' WHERE rowid!=?)
REAL
 EXISTS
weekday 
ousli
aes128
2026-04-09 12:25:13 8fa8248e303219400c646a885e36dfc52eae33d83f4412e3f369b2be5373aapl
Divide
unknown datatype: %Q
cannot %s %s \"%s\"
UPDATE \"%w\".sqlite_master SET sql = sqlite_add_constraint(sql, %.*Q, -1) WHERE type='table' AND tbl_name=%Q COLLATE nocase
k PRIMARY KEY, v
%z, %Q HIDDEN, %s HIDDEN)
open destination failed for %d\n
-conch
F_GETLKPID undefined or not supported, _sqlite3_lockstate falling back to F_GETLK
dflt_value
TABLE
foreign key on %s should reference only one column of table %T
cannot use window functions in recursive queries
usermerge
database corruption page %u of %s
NotFound
Null
DELETE FROM '%q'.'%q_data' WHERE id>=? AND id<=?
%s contentless fts5 table: %s
_parent
MAX_PAGE_SIZE=65536
executing sql '%s' returned error %x with message:'%s'\n
IFindKey
SqlExec
concat
DELETE FROM %Q.'%q_segments' WHERE blockid BETWEEN ? AND ?
uuid
This version of the encryption extension does not support an activation passphrase
OpenWrite
off
PerfPowerServices
sinh
asc
fts5vocab: unknown table type: %Q
SAVEPOINT changeset
?
Sequence
SCAN %s%s%s
iciti
ENABLE_UPDATE_DELETE_LIMIT
incremental_vacuum enabled with a max rootpage of zero
Checkpoint
AggStep1
porter
S
SorterData
AND 
IfEmpty
40f-21a-21d
ieee754
unsafe use of %#T()
unicode
MAX_LIKE_PATTERN_LENGTH=50000
sqlite3changeset_apply(): table %s has %d columns, expected %d or more
SQLITE_TMPDIR
expr_implies_expr
unable to open database file
main
Compression method %ld not currently supported for operationType %ld
FkIfZero
last_insert_rowid
MAX_LENGTH=2147483645
%!.*g
free space corruption
application_id
no such window: %s
UNION ALL
Return
%!.15g
floor
%!0.15g
UTF8
database table is locked
ENABLE_FTS3_PARENTHESIS
BEGIN EXCLUSIVE;\nCOMMIT;\n
see-cccrypt
comment
narg
SNaN
aggregate functions are not allowed in the GROUP BY clause
LIMIT
ousness
SQLITE_
denying fileSize on invalidated fd %d
SetStoreUpdateService
filename
CREATE TABLE IF NOT EXISTS 
PRAGMA schema_version
Tree %u page %u cell %u: 
SELECT raise(ABORT,%Q) FROM \"%w\".\"%w\"
from
pwrite64
failed to break stale lock on %s, %s\n
-mj%06X9%02X
Function
Environment override of cache_size %d -> %d
data_version
fullfsync
too many columns in result set
pipe failed for %d\n
Destroy
issisi
SELECT %s FROM %s T WHERE T.%Q >= ? AND T.%Q <= ? ORDER BY T.%Q ASC
USE_URI
ieee754_to_blob
unix-posix
seekAndWrite
%s.lock
revoked
USING
unrecognized option: \"%.*s\"
ENABLE_SETLK_TIMEOUT
PureFunc
OpenEphemeral
invalid page number %u
\\u000b
not authorized
LAST
USE TEMP B-TREE FOR LAST %d TERMS OF ORDER BY
SQLITE_ENABLE_THREAD_ASSERTIONS
BEGIN DEFERRED; PRAGMA schema_version;
generated columns
Invalid parameter to environment variable SQLITE_MALLOC_ZONE: \"%s\". Supported values are \"default\" and \"custom\"\n
line %d: unterminated %c-quoted field\n
no such index: %s
20b:20e
%sc%d TEXT
PRAGMA \"%w\".page_count
Skipping vnode guard based on exemption path %s for file: %s
Multiply
Bad ptr map entry key=%u expected=(%u,%u) got=(%u,%u)
table_xinfo
(null)
ENABLE_FTS3
auto_vacuum
auto_vacuum=1
SQLITE_MIN_CACHE_SIZE
python
CREATE TABlE vocab(term, doc, cnt)
%lld
psow
SeekRowid
ParseSchema
VRename
numeric
see-
interrupted
error in %s %s after %s: %s
abs
json_array_insert
SELECT %s ORDER BY rowid %s
T.%Q
RtreeMatchArg
DEFAULT_WORKER_THREADS=0
%s_%02d.db
ieee754_exponent
BitNot
cannot modify %s because it is a view
Real
MemMax
ro
unable to identify the object to be reindexed
IdxInsert
unknown
rw
reserved fts5 column name: %s
 OR 
pragma_list
ORDER BY may not be used with non-aggregate %#T()
more than one '%s' parameter
Query: %s\n Execution Time: %llu ms\n
SQLITE_ACCEPTABLE_RATIO_VM_STEP_TO_STEP
%s cannot use variables
unistr
fts3
secure-delete
fts5_locale() requires locale=1
anci
IsNull
JSON cannot hold BLOB values
DELETE FROM %Q.'%q_segdir' WHERE level = ?
ATTACH '%q' AS '%q'; -- clock=%d\n
JSON path too deep
unknown database %T
upper
ant
index_list
timediff
no such function: %s
SQLITE_SQLLOG_CONDITIONAL
(
recovered %d frames from WAL file %s
p3
$
SELECT max( level %% 1024 ) FROM %Q.'%q_segdir'
VFilter
CREATE %s %.*s
use DROP TABLE to delete table %s
automerge=
ALTER TABLE %Q.'%q_docsize'  RENAME TO '%q_docsize';
RELEASE changeset
Goto
REUSE LIST SUBQUERY %d
qualified table names are not allowed on INSERT, UPDATE, and DELETE statements within triggers
,?
cannot DELETE from contentless fts5 table: %s
parent
unrecognized order: %s
error in tokenizer constructor
DELETE FROM '%q'.'%q_parent' WHERE nodeno = ?1
corrupted
%s-wal
create
OpenRead
sz=[0-9]*
max rootpage (%u) disagrees with header (%u)
ANY(%s)
SQLITE_ENABLE_FILE_ASSERTIONS
id INTEGER PRIMARY KEY, block BLOB
no such table column: %s.%s
short_column_names
no such table: 
SeekLE
-- 
 TEXT
min
separators=
ful
ical
Gt
PRIMARY KEY missing on table %s
json_error_position
UPDATE OR FAIL %Q.'%q_segdir' SET level=? WHERE level=-1
/NoteStore.sqlite
mediaanalysisd
SELECT*FROM\"%w\".%s WHERE %s ORDER BY rowid
ORDER BY clause
<b>...</b>
MALLOC_SOFT_LIMIT=1024
current_time
DEFAULT_WAL_SYNCHRONOUS=1
lstat
rtree
DEFAULT_PAGE_SIZE=4096
ENABLE_UNKNOWN_SQL_FUNCTION
mremap
USE TEMP B-TREE FOR %s
SCAN
current_timestamp
__langid
{%lld
DEFAULT_LOOKASIDE=1200,40
Close
CORRELATED 
NUM
malformed detail=... directive
fsync
OpenPseudo
idx
DELETE FROM '%q'.'%q_idx' WHERE segid=?
SeekLT
missing datatype for %s.%s
UTF16le
non-deterministic use of %s() in %s
prefix length out of range (max 999)
SELECT * FROM %Q.'%q_rowid'
yes
ptr
IMDPersistence
temp_store
index %s stores an imprecise floating-point value for row 
unrecognized token: \"%s\"
contentless_unindexed=1 requires a contentless table
close
seekAndWrite: updated file size hint from %lld to actual size %lld
unknown database %s
unordered*
output file already exists
DELETE
siX
on
ieee754_from_int
MERGE (%s)
lower
ln
warning message
pragma encoding
 %Q
addr
unknown column \"%s\" in foreign key definition
jsonb_object
fts5: syntax error near \"%.*s\"
MAX_COLUMN=2000
int32
SELECT %s,%s FROM \"%w\".\"%w\", \"%w\".\"%w\" WHERE %s AND (%z)
) VALUES(?
sqllogFindAttached(): error in \"PRAGMA database_list\"
CREATE TRIGGER
unopened
cannot VACUUM - SQL statements in progress
DELETE FROM %Q.sqlite_master WHERE name=%Q AND type='trigger'
cannot create %s trigger on view: %S
L* N* Co
is
UPDATE \"%w\".sqlite_master SET sql = sqlite_drop_column(%d, sql, %d) WHERE (type=='table' AND tbl_name=%Q COLLATE nocase)
affected by unexpected operations
readonly_shm
RowSetAdd
p1
authorizer malfunction
TEXT
Pythonsqlite3
no such rowid: %lld
ROWID
no such column: %s
SELECT %s WHERE rowid=?
cannot open '%s' for reading
Paper
queries_persist
AggInverse
all VALUES must have the same number of terms
PRAGMA %Q.page_size
(NULL)
/AddressBook/AddressBook.sqlitedb
substr
ation
SELECT nodeno FROM %Q.'%q_rowid' WHERE rowid=?1
truncate failed on '%s' with errno %d\n
unable to open a temporary database file for storing temporary tables
*
expressions prohibited in PRIMARY KEY and UNIQUE constraints
json_object() requires an even number of arguments
DELETE FROM %Q.'%q_data';DELETE FROM %Q.'%q_idx';
rtree constraint failed: %s.(%s<=%s)
 USING 
nullif
SELECT %s FROM %s AS T
%s;\n
decompressor
TableLock
unique
virtual tables cannot use computed columns
<expr>
unrecognized parameter: %s
Too many columns for an rtree table
sqlite_schema
glob
%s.rowid
substring
DELETE FROM %Q.'%q_docsize' WHERE id=?
SAVEPOINT changeset_apply
MJ collide: %s
NotNull
-9e999
hex literal too big: %s%#T
no such trigger: %S
UNIQUE constraint failed: %s.%s
unixTruncateDatabase() failed with %d for replacing '%s' with flags %x\n
IfNullRow
count
w
jsonb_group_object
,'%s',char(13))
backupd
Offset
cache
DELETE FROM %Q.'%q_segdir' WHERE level = ? AND idx = ?
SAVEPOINT fts3
iviti
922337203685477580
Concat
cannot commit transaction - SQL statements in progress
contentless_delete
btreeInitPage() returns error code %d
module_list
table %S has %d columns but %d values were supplied
sqlite_stat3
Unknown operation type %ld
write failed (%d)
fts3tokenize
%z,?%d
Abortable
table_info
char*
ltrim
remove_diacritics=2
SELECT %s FROM %s T WHERE T.%Q <= ? AND T.%Q >= ? ORDER BY T.%Q DESC
denying write to invalidated fd %d
50000
illegal first argument to %s
automerge
ness
_rowid
internal
checkpointed
ON clause
wrong # of entries in index 
constraint failed
CREATE TABLE x(%.*s INT
NullRow
carray
text
SELECT idx, start_block, leaves_end_block, end_block, root FROM %Q.'%q_segdir' WHERE level BETWEEN ? AND ?ORDER BY level DESC, idx ASC
Rtree depth out of range (%d)
Affinity
securityd
UNION
@
DELETE FROM %Q.'%q_docsize' WHERE docid = ?
%s constraint failed
RELEASE
%#Q
another row available
?1, (CASE WHEN ?2=X'' THEN NULL ELSE ?2 END)
%s-journal
pragma auto_vacuum
sql_error
String8
AUTOMATIC PARTIAL COVERING INDEX
malformed JSON
%#T() may not be used as a window function
%c?)
 VIRTUAL TABLE INDEX 
RETURNING may not use \"TABLE.*\" wildcards
unixepoch
unterminated string
THREADSAFE=2
broke stale lock on %s\n
-mj
no such database: %s
stat_init
log10
misuse
string_agg
iti
%Q.'%q_%s'
VUpdate
FOREIGN KEY
%s RETURNING is not available on virtual tables
cannot create triggers on virtual tables
contentless_unindexed
ement
%llu
json_array_length
cannot open table without rowid: %s
database schema is locked: %s
%d columns assigned %d values
AFTER
instr
SELECT * FROM \"%w\".\"%w_rowid\" WHERE rowid=?1
BEGIN DEFERRED; PRAGMA schema_version; COMMIT;
Add
[%lld]
SELECT*FROM\"%w\".\"%w\"
NOCASE
restart
cannot create trigger on system table
no such %s mode: %s
 VALUES(
%s is %u but should be %u
sqlite_attach
ive
hashsize
Wrong number of entries in %%%s table - expected %lld, actual %lld
CREATE TABLE x(type TEXT,schema TEXT,name TEXT,wr INT,subprog TEXT,stmt HIDDEN);
ColumnsUsed
.%.*s
RAISE() may only be used within a trigger-program
%r 
ic
json
writable_schema
reset
median
SELECT segid, term, (pgno>>1), (pgno&1) FROM %Q.'%q_idx' WHERE segid=%d ORDER BY 1, 2
CHECK constraint failed in %s
unistr_quote
fts5: syntax error near \"%.1s\"
tokenchars
 IS ?
SQLITE_SQLLOG_REUSE_FILES
:auto: (not held)
ReadCookie
pwrite
9.0e999
cannot create triggers on shadow tables
log2
SELECT pgno FROM '%q'.'%q_idx' WHERE segid=? AND term>? ORDER BY term ASC LIMIT 1
mkdir
/*sort*/
foreign_key_check
JSON nested too deep
SELECT 1 FROM %Q.'%q_segments' WHERE blockid=? AND block IS NULL
compression_stream_process alpha failed for %d\n
Filter
enableTelemetry=%s nSpill=%{public,signpost.telemetry:number1,name=rc}d writes=%{public,public,signpost.telemetry:number2}d
startTime=%{signpost.description:begin_time}llu path=%s
Failed to open temporary file at path %s: %s
spilled %d pages during execution of [%s]
startTime=%{signpost.description:begin_time}llu db=%{public}p query=%{public,signpost.telemetry:string1,name=query}s
unable to close due to unfinalized statements or unfinished backups
open
rc=%{public}d db=%{public}p errMsg=%{public}s
Query: %s\n Execution Time: %llu ms\n
%s
_CS_DARWIN_USER_TEMP_DIR was deleted out from underneath this process. This is illegal and likely to cause crashes and data corruption.
locking protocol: lockstate:%d, bShmUnreliable:%d, readOnly:%d
Error: %{errorMessage,public}s coalition: %{coalition,public}s database: %{database,public}s query: %{query,public}s
%d scan steps for %d row steps in [%s]
pcache replacing page with non-zero refcount
SQL Error
close
seekAndWrite(%lld, %d): improbable offset+len for file with size hint %lld
No temporary directory is accessible.  This is not a legitimate configuration.  Either the process environment or its sandbox is misconfigured.  Various library routines will error out abruptly.
libsqlite: Error: Failed WAL locking protocol.
enableTelemetry=%s rc=%{public,signpost.telemetry:number1,name=rc}d runCount=%{public}d nScan=%{public}d nAutoindex=%{public}d nSort=%{public}d nSpill=%{public}d nStep=%{public}d errMsg=%{public}s nVmStep=%{public,signpost.telemetry:number2
startTime=%{signpost.description:begin_time}llu db=%p
flagged inefficient query yielding %d results (expected vdbe steps ≤ %d, actual: %d) [%s]
cache_spill
Error: %{errorMessage,public}s coalition: %{coalition,public}s
xRekey overwriting %{public}s page at index %d
TraceSQL(%p): %s\n
execute
user 'setup'(248) opening database with SQLITE_OPEN_READWRITE
seekAndWrite(%lld, %d): improbable offset+len for file with observed size %lld
%d automatic index rows in [%s]
sort without index in [%s]
```
