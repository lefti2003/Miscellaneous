# A RouteTrieNode will be similar to our autocomplete TrieNode...
# with one additional element, a handler.

class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, path_list, handler_input):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self.root
        for path in path_list:
            if path not in current.children:
                current.children[path] = RouteTrieNode()
            current = current.children[path]
        current.handler = handler_input

        return current

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current = self.root
        for path in path_list:
            if path not in current.children:
                return None
            else:
                current = current.children[path]
        return current.handler
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.


class RouteTrieNode:

    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, part):
        # Insert the node as before
        self.children[part] = RouteTrieNode()
        # The Router class will wrap the Trie and handle


class Router:

    def __init__(self, root_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routetrie = RouteTrie()
        self.routetrie.root.handler = root_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        #print(f"path_l={path_list}")
        node = self.routetrie.insert(path_list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        if not self.routetrie.find(path_list):
            return "Not found handler"
        else:
            return self.routetrie.find(path_list)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        return [y for y in path.split("/") if y]


# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route
#router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router = Router("root handler")
router.add_handler("/home/about", "about handler") # add a route
# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one