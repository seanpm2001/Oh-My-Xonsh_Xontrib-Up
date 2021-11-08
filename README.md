# UP! - the fast way to go up directories in xonsh

Tired of attaching "balloons" to your `cd` command to go up directories?

`cd ..`, `cd ../..`, `cd ../../..`, `cd ../../../..`, `cd ../../../../../../../../../../../../../..`?

Tired of creating weird aliases like `cd..4`, `cd..12`, ... `cd..100` to navigate up directories?

Now you can use `up`!

Type `up` to go up one directory. Type `up 2` to go up two directories. Type
`up 42` to go up forty-two directories. It's that easy.

No more defining an alias for `cd ../../../../../../..`.  Just type `up 7`.

```shell
$ # cd ../../..
$ up 3
```

You can also get the path that `up` will produce by using `upp` (up path).
This lets you see what directory up will produce.

```shell
$ # pushd -q .; cd ../../../..; echo $PWD; popd -q
$ upp 4
```

Listing ancestor directories with `ls` requires balloons, but not anymore.
A simple way to list ancestor dirs is with `lsup`, which forwards on any options to `ls`.

```shell
$ # long list everything 3 dirs up (ie: `ls -opts ../../..`)
$ lsup -laFGh 3
```

## Commands

| Command | Description                                |
|:--------|:-------------------------------------------|
| `up`    | Travel up any number of directories        |
| `upp`   | Get the path of an ancestor directory      |
| `lsup`  | List the contents of an ancestor directory |

## Install

Install up via `xpip`:

```shell
xpip install xontrib-up
```

Add this to your `~/.config/xonsh/rc.xsh` or `~/.xonshrc`:

```shell
xontrib load up
```

[xonsh]: https://xon.sh
