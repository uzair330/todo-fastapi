type TodosType = {
  id: number;
  task: string;
  status: string;
}

const Todos = async () => {
  const res = await fetch(`${process.env.BACKEND_URL}/api/todos`);
  const data: TodosType[] = await res.json();
  return data;  
  console.log(process.env.BACKEND_URL);
  

}

const Home = async () => {
  const todos = await Todos();
  return (
    <div className="flex flex-col mx-auto max-w-7xl mt-24">
    {
        Array.isArray(todos) ? todos.map((todo: TodosType) => (
            <div key={todo.id}>
                <p>Task: {todo.task}</p>
                <p>Status: {todo.status}</p>
            </div>
        )) : <p>Error: todos is not an array</p>
    }
</div>
  );
}

export default Home;
