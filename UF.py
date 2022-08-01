class UF:

    def __init__(self, n, id=None):
        self.n = n
        if id:
            self.id = id
        else:
            self.id = []
            self.sz = []
            for i in range(n):
                self.id.append(i)
                self.sz.append(1)

    def get_root(self, p):
        child = p
        parent = self.id[p]
        while parent != child:
            child = parent
            parent = self.id[child]
        return parent

    def find(self, p, q):
        if self.get_root(p) == self.get_root(q):
            return True
        return False

    def union(self, p, q):
        p_root = self.get_root(p)
        q_root = self.get_root(q)
        if p_root == q_root:
            return
        else:
            if self.sz[q_root] > self.sz[p_root]:
                self.id[p_root] = q_root
                self.sz[q_root] = self.sz[q_root] + self.sz[p_root]
            else:
                self.id[q_root] = p_root
                self.sz[p_root] = self.sz[p_root] + self.sz[q_root]
